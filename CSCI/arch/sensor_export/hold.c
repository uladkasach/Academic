
static void set_time_now_to_predefined(){
    ESP_LOGI(TAG_RETREIVE, "(*) attempting to update time now to a predefined value!")
    struct timeval now;
    int rc;

    now.tv_sec=866208142;
    now.tv_usec=290944;

    rc=settimeofday(&now, NULL);
    if(rc==0) {
        ESP_LOGI(TAG_RETREIVE, "    time update successful")
    }
    else {
        ESP_LOGE(TAG_RETREIVE, "    time update failed, errno = %d\n",errno)
    }
}


ESP_LOGI(TAG_OUTPUT, "RAM left %d", esp_get_free_heap_size());
