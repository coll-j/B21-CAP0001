package com.dicoding.picodiploma.thumbs.networking.endpoints

import com.dicoding.picodiploma.thumbs.networking.model.User
import okhttp3.RequestBody
import okhttp3.ResponseBody
import retrofit2.Call
import retrofit2.Response
import retrofit2.http.*

interface AuthenticationEndpoints {
    @POST("/auth/login")
    suspend fun login(@Body requestBody: RequestBody): Response<ResponseBody>
}