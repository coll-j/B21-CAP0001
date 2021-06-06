package com.dicoding.picodiploma.thumbs.networking.controller

import com.dicoding.picodiploma.thumbs.networking.repository.AuthenticationRepository

object AuthenticationController {
    suspend fun login(username: String, password: String) {
        AuthenticationRepository.login("kuuhaku86", "yohan123")
    }
}
