package com.dicoding.picodiploma.thumbs.networking.model

data class Response (
    val auth_token: String = "",
    val code: Int = 0,
    val data: Any,
    val message: String = "",
    val status: String = ""
)
