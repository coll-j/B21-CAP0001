package com.dicoding.picodiploma.thumbs.networking.repository

import android.util.Log
import com.dicoding.picodiploma.thumbs.networking.ServiceBuilder
import com.dicoding.picodiploma.thumbs.networking.endpoints.AuthenticationEndpoints
import com.dicoding.picodiploma.thumbs.networking.model.Response
import com.google.gson.Gson
import com.google.gson.GsonBuilder
import com.google.gson.JsonParser
import okhttp3.MediaType.Companion.toMediaTypeOrNull
import okhttp3.RequestBody
import okhttp3.RequestBody.Companion.toRequestBody
import org.json.JSONObject

object AuthenticationRepository {
    val request = ServiceBuilder.buildService(AuthenticationEndpoints::class.java)

    suspend fun login(username: String, password: String): Response? {

        val field = hashMapOf("username" to username, "password" to password)
        val response = request.login(requestMaker(field))

        return if (response.isSuccessful) {
            val gson = GsonBuilder().setPrettyPrinting().create()
            val prettyJson = gson.toJson(
                JsonParser.parseString(
                    response.body()?.string()
                )
            )
            val newGson: Gson = Gson()
            newGson.fromJson(prettyJson, Response::class.java)
        } else {
            Log.e("RETROFIT_ERROR", response.code().toString())
            null
        }
    }

    suspend fun register(username: String, password: String, email: String): Response? {

        val field = hashMapOf("username" to username, "password" to password, "email" to email)
        val response = request.register(requestMaker(field))

        return if (response.isSuccessful) {
            val gson = GsonBuilder().setPrettyPrinting().create()
            val prettyJson = gson.toJson(
                JsonParser.parseString(
                    response.body()?.string()
                )
            )
            val newGson: Gson = Gson()
            newGson.fromJson(prettyJson, Response::class.java)
        } else {
            Log.e("RETROFIT_ERROR", response.code().toString())
            null
        }
    }

    private fun requestMaker(map: HashMap<String, String>): RequestBody {
        val jsonObject = JSONObject()

        for ((key, value) in map) {
            jsonObject.put(key, value)
        }

        val jsonObjectString = jsonObject.toString()

        return jsonObjectString.toRequestBody("application/json".toMediaTypeOrNull())
    }

}