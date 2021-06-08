package com.dicoding.picodiploma.thumbs.whutsapp

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.bumptech.glide.Glide
import com.bumptech.glide.request.RequestOptions
import com.dicoding.picodiploma.thumbs.databinding.ItemWaBinding

class ListWaAdapter(private val listUserWa: ArrayList<UserWa>) : RecyclerView.Adapter<ListWaAdapter.ListViewHolder>(){

    private var onItemClickCallback: OnItemClickCallback? = null

    fun setOnItemClickCallback(onItemClickCallback: OnItemClickCallback) {
        this.onItemClickCallback = onItemClickCallback
    }

    inner class ListViewHolder(private val binding: ItemWaBinding) : RecyclerView.ViewHolder(binding.root)  {
        fun bind(user: UserWa) {
            with(binding){
                Glide.with(itemView.context)
                    .load(user.photo)
                    .apply(RequestOptions().override(55, 55))
                    .into(imgPhoto)
                tvItemName.text = user.name
                tvItemDetail.text = user.detail
                tvItemTime.text = user.time

                itemView.setOnClickListener { onItemClickCallback?.onItemClicked(user) }
                val user = UserWa(
                    user.name,
                    user.detail,
                    user.time,
                    user.photo
                )
//                val intentUserChat = Intent(whutsAppChatActivity::class.java)
//                intentUserChat.putExtra(whutsAppChatActivity, user)
//                startActivity(intentUserChat)
            }
        }
    }

    interface OnItemClickCallback {
        fun onItemClicked(data: UserWa)
    }

    override fun onCreateViewHolder(viewGroup: ViewGroup, i: Int): ListViewHolder {
        val binding = ItemWaBinding.inflate(LayoutInflater.from(viewGroup.context), viewGroup, false)
        return ListViewHolder(binding)
    }

    override fun onBindViewHolder(holder: ListViewHolder, position: Int) {
        holder.bind(listUserWa[position])
    }

    override fun getItemCount(): Int = listUserWa.size

}