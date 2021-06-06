package com.dicoding.picodiploma.thumbs.networking.repository

import android.util.Log
import com.dicoding.picodiploma.thumbs.networking.ServiceBuilder
import com.dicoding.picodiploma.thumbs.networking.endpoints.AuthenticationEndpoints
import com.dicoding.picodiploma.thumbs.networking.model.Response
import com.dicoding.picodiploma.thumbs.networking.model.User
import com.google.gson.Gson
import com.google.gson.GsonBuilder
import com.google.gson.JsonParser
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import okhttp3.MediaType.Companion.toMediaTypeOrNull
import okhttp3.RequestBody.Companion.toRequestBody
import org.json.JSONObject
import java.lang.Exception

object AuthenticationRepository {
    val request = ServiceBuilder.buildService(AuthenticationEndpoints::class.java)

    suspend fun login(username: String, password: String){
        val jsonObject = JSONObject()
        jsonObject.put("username", username)
        jsonObject.put("password", password)

        val jsonObjectString = jsonObject.toString()
        val requestBody = jsonObjectString.toRequestBody("application/json".toMediaTypeOrNull())

        val response = request.login(requestBody)

        withContext(Dispatchers.Main) {
            if (response.isSuccessful){
                val gson = GsonBuilder().setPrettyPrinting().create()
                val prettyJson = gson.toJson(
                    JsonParser.parseString(
                        response.body()?.string()
                    )
                )
                val newGson: Gson = Gson()
//                    Convert the response to response model
                val result = newGson.fromJson(prettyJson, Response::class.java)
//                    Get the data (convert to specific data class)
                val data = newGson.fromJson(result.data.toString(), User::class.java)
//                    Log.d("Result", data.toString())
//                    Log.d("Pretty Printed JSON :", prettyJson)

            } else {
                Log.e("RETROFIT_ERROR", response.code().toString())
//                returnData("RETROFIT_ERROR ${response.code()}")
            }
        }
    }
}