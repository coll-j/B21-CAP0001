package com.dicoding.picodiploma.thumbs

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import com.dicoding.picodiploma.thumbs.databinding.ActivityMainBinding
import com.dicoding.picodiploma.thumbs.whutsapp.whutsAppActivity

class MainActivity : AppCompatActivity(), View.OnClickListener {

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

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