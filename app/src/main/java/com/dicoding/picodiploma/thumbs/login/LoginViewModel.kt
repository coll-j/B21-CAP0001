package com.dicoding.picodiploma.thumbs.login

import android.app.Application
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.dicoding.picodiploma.thumbs.networking.model.User
import com.dicoding.picodiploma.thumbs.networking.repository.AuthenticationRepository
import com.google.gson.Gson
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

class LoginViewModel(application: Application) : AndroidViewModel(application) {
    private val scope = CoroutineScope(Dispatchers.IO)
    private val _user = MutableLiveData<User>()
    private val newGson: Gson = Gson()

    val user: LiveData<User>
        get() = _user

    fun login(username: String, password: String) {
        scope.launch {
            val result = AuthenticationRepository.login(username, password)
            if(result != null && result.code == 200){
                withContext(Dispatchers.Main){
                    _user.value = newGson.fromJson(result.data.toString(), User::class.java)
                }
            }else{
                withContext(Dispatchers.Main){
                    _user.value = null
                }
            }
        }
    }
}