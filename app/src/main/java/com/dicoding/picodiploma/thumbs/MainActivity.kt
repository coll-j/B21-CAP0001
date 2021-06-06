package com.dicoding.picodiploma.thumbs

import android.os.Bundle
import android.util.Log
import android.view.Menu
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.ViewModelProvider
import androidx.recyclerview.widget.LinearLayoutManager
import com.dicoding.picodiploma.thumbs.databinding.ActivityMainBinding
import com.dicoding.picodiploma.thumbs.login.LoginViewModel


class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding
    private val list = ArrayList<userWa>()
    private lateinit var loginViewModel: LoginViewModel
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.rvWa.setHasFixedSize(true)
        list.addAll(getListUserWa())
        showRecyclerList()

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
    }

    fun getListUserWa(): ArrayList<userWa> {
        val dataName = resources.getStringArray(R.array.data_name)
        val dataDetail = resources.getStringArray(R.array.data_detail)
        val dataTime = resources.getStringArray(R.array.data_time)
        val dataPhoto = resources.getStringArray(R.array.data_photo)
        val listUserWa = ArrayList<userWa>()
        for (position in dataName.indices) {
            val user = userWa(
                dataName[position],
                dataDetail[position],
                dataTime[position],
                dataPhoto[position]
            )
            listUserWa.add(user)
        }
        return listUserWa
    }

    private fun showRecyclerList() {
        binding.rvWa.layoutManager = LinearLayoutManager(this)
        val listHeroAdapter = ListWaAdapter(list)
        binding.rvWa.adapter = listHeroAdapter
    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        menuInflater.inflate(R.menu.menu_main, menu)
        return super.onCreateOptionsMenu(menu)
    }

}