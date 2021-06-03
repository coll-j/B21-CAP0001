package com.dicoding.picodiploma.thumbs

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.bumptech.glide.Glide
import com.bumptech.glide.request.RequestOptions
import com.dicoding.picodiploma.thumbs.databinding.ItemWaBinding

class ListWaAdapter(private val listUserWa: ArrayList<userWa>) : RecyclerView.Adapter<ListWaAdapter.ListViewHolder>(){

    class ListViewHolder(private val binding: ItemWaBinding) : RecyclerView.ViewHolder(binding.root)  {
        fun bind(userwa: userWa) {
            with(binding){
                Glide.with(itemView.context)
                    .load(userwa.photo)
                    .apply(RequestOptions().override(55, 55))
                    .into(imgPhoto)
                tvItemName.text = userwa.name
                tvItemDetail.text = userwa.detail
                tvItemTime.text = userwa.time
            }
        }
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