package com.dicoding.picodiploma.thumbs

import android.os.Bundle
import android.util.Log
import android.view.Menu
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.ViewModelProvider
import androidx.recyclerview.widget.LinearLayoutManager
import com.dicoding.picodiploma.thumbs.databinding.ActivityMainBinding
import com.dicoding.picodiploma.thumbs.login.LoginViewModel

import android.content.Intent
import android.view.View
import com.dicoding.picodiploma.thumbs.whutsapp.whutsAppActivity

class MainActivity : AppCompatActivity(), View.OnClickListener {

    private lateinit var binding: ActivityMainBinding
    private lateinit var loginViewModel: LoginViewModel

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

//        example calling viewmodel of authentication
        loginViewModel = ViewModelProvider(this)[LoginViewModel::class.java]
        loginViewModel.login("", "")
        loginViewModel.user.observe(this, { user ->
            if(user !== null){
                Log.d("observe", user.toString())
            }else{
                Log.d("observe", "null")
            }
        })
        binding.imgBtnWa.setOnClickListener(this)
    }

    override fun onClick(v: View?) {
        when(v?.id){
            R.id.imgBtn_wa -> {
                val moveIntent = Intent(this@MainActivity, whutsAppActivity::class.java)
                startActivity(moveIntent)
            }
            R.id.imgBtn_twitter ->{

            }
            R.id.imgBtn_browser -> {

            }
            R.id.imgBtn_setting ->{

            }
        }
    }
}