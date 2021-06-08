
package com.dicoding.picodiploma.thumbs.whutsapp

import android.os.Parcelable
import kotlinx.parcelize.Parcelize

@Parcelize
data class UserWa(
    var name: String,
    var detail: String,
    var time: String,
    var photo:String
) : Parcelable