package com.dicoding.picodiploma.thumbs.whutsapp.chat

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.dicoding.picodiploma.thumbs.databinding.ActivityWhutsAppChatBinding
import com.dicoding.picodiploma.thumbs.whutsapp.UserWa

class whutsAppChatActivity : AppCompatActivity() {

    private lateinit var binding : ActivityWhutsAppChatBinding

    companion object
    {
        const val EXTRA_USER = "0"
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityWhutsAppChatBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val user : UserWa =  intent.getParcelableExtra<UserWa>(EXTRA_USER) as UserWa
        binding.idTvName.text = user.name
        binding.imgPhoto.setImageResource(user.photo.toInt())
//        binding.imgPhoto = user.photo
    }
}