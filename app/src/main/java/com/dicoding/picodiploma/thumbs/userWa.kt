package com.dicoding.picodiploma.thumbs

import android.os.Parcelable
import kotlinx.parcelize.Parcelize

@Parcelize
data class userWa(
    var name: String,
    var detail: String,
    var time: String,
    var photo:String
) : Parcelable
