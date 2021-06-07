package com.dicoding.picodiploma.thumbs.whutsapp

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.Menu
import androidx.recyclerview.widget.LinearLayoutManager
import com.dicoding.picodiploma.thumbs.R
import com.dicoding.picodiploma.thumbs.databinding.ActivityWhutsAppBinding
import com.dicoding.picodiploma.thumbs.whutsapp.chat.whutsAppChatActivity

class whutsAppActivity : AppCompatActivity() {

    private lateinit var binding: ActivityWhutsAppBinding
    private val list = ArrayList<userWa>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityWhutsAppBinding.inflate(layoutInflater)
        setContentView(binding.root)
        supportActionBar?.title = "WhutsApp"

        binding.rvWa.setHasFixedSize(true)
        list.addAll(getListUserWa())
        showRecyclerList()
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
        val listWaAdapter = ListWaAdapter(list)
        binding.rvWa.adapter = listWaAdapter

        listWaAdapter.setOnItemClickCallback(object : ListWaAdapter.OnItemClickCallback{
            override fun onItemClicked(data: userWa) {
                showSelectedUser(user = data)
            }
        })
    }

    private fun showSelectedUser(user: userWa) {
        userWa(
            user.name,
            user.detail,
            user.time,
            user.photo
        )

        val intent = Intent(this, whutsAppChatActivity::class.java)
//        intent.putExtra(whutsAppChatActivity, user)
        startActivity(intent)
    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        menuInflater.inflate(R.menu.menu_main, menu)
        return super.onCreateOptionsMenu(menu)
    }
}