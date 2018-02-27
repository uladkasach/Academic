/*
    This code is based on the LwIP SNTP example
*/
// glibc dependencies:
#include <string.h>
#include <time.h>
#include <sys/time.h>

// espress IDF dependencies
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "freertos/event_groups.h"
#include "esp_system.h"
#include "esp_wifi.h"
#include "esp_event_loop.h"
#include "esp_log.h"
#include "esp_attr.h"
#include "esp_sleep.h"
#include "nvs_flash.h"

#include "lwip/err.h"
#include "apps/sntp/sntp.h"


/*
    Define WIFI SSID and PASS for usage in wifi
*/
#define EXAMPLE_WIFI_SSID "Beach Bus" // iwgetid -r
#define EXAMPLE_WIFI_PASS "Waterfall"

/* FreeRTOS event group to signal when we are connected & ready to make a request */
static EventGroupHandle_t wifi_event_group;

/* The event group allows multiple bits for each event,
   but we only care about one event - are we connected
   to the AP with an IP? */
const int CONNECTED_BIT = BIT0;

static const char *TAG = "app";
static const char *TAG_RETREIVE = "retreive";
static const char *TAG_OUTPUT = "output";

/* Variable holding number of times ESP32 restarted since first boot.
 * It is placed into RTC memory using RTC_DATA_ATTR and
 * maintains its value when ESP32 wakes from deep sleep.
 */
RTC_DATA_ATTR static int boot_count = 0;

/*
    variables globally defining task handlers
*/
xTaskHandle time_update_task_handle;
xTaskHandle time_output_task_handle;

static void request_time_update(void);
static void initialize_utilities(void);
static void initialize_non_volatile_storage(void);
static void update_time_with_sntp(void);
static void wait_until_time_updated(void);
static void start_wifi_connection(void);
static void stop_wifi_connection(void);
static void wait_until_wifi_connected(void);
static void initialise_wifi(void);
static esp_err_t event_handler(void *ctx, system_event_t *event);

/*
void do_thing_task( void* p ) // gotta have a void pointer as parameter even if unused
{
while( true ) // gotta have infinite loop
    {
        // do things
        ESP_LOGI(TAG, "Boot count: %d", boot_count);
        vTaskDelay( 1000 / portTICK_PERIOD_MS ) // wait / yield time to other tasks
    }
}
*/

static void task_update_internal_time_with_sntp( void *pvParameters )
{
    for( ;; )
    {
        ESP_LOGI(TAG_RETREIVE, "(!) Starting Update of Internal Wall-Clock Time Again...")

        initialize_utilities();
        request_time_update();

        const int sleep_sec = 10; // 10 seconds
        ESP_LOGI(TAG_RETREIVE, "update of wall clock time has completed. entering task wait for %d seconds", sleep_sec);
        vTaskDelay( sleep_sec * 1000 / portTICK_PERIOD_MS ); // wait / yield time to other tasks
    }
}


static void display_internal_time( void *pvParameters )
{
    for( ;; )
    {
        ESP_LOGI(TAG_OUTPUT, "(!) Displaying Internal Time...")

        wait_until_time_updated(); // ensure time is updated before displaying it

        time_t now;
        struct tm timeinfo;
        time(&now);
        char strftime_buf[64];

        // Set timezone to Eastern Standard Time and print local time
        setenv("TZ", "EST5EDT,M3.2.0/2,M11.1.0", 1);
        tzset();
        localtime_r(&now, &timeinfo);
        strftime(strftime_buf, sizeof(strftime_buf), "%c", &timeinfo);
        ESP_LOGI(TAG, "The current date/time in New York is: %s", strftime_buf);

        const int sleep_millisec = 1000;
        ESP_LOGI(TAG_OUTPUT, "output of time completed. entering task wait for %d milliseconds", sleep_millisec);
        vTaskDelay( sleep_millisec / portTICK_PERIOD_MS ); // wait / yield time to other tasks
    }
}


void app_main()
{
    ++boot_count;
    ESP_LOGI(TAG, "Boot count: %d", boot_count);

    BaseType_t xReturned_updateTask;
    xReturned_updateTask = xTaskCreate(task_update_internal_time_with_sntp,  // pointer to function
                "time_update_task",        // Task name string for debug purposes
                8000,            // Stack depth as word
                NULL,           // function parameter (like a generic object)
                1,              // Task Priority (Greater value has higher priority)
                &time_update_task_handle);  // Task handle

    BaseType_t xReturned_outputTask;
    xReturned_outputTask = xTaskCreate(display_internal_time,  // pointer to function
                "time_output_task",        // Task name string for debug purposes
                8000,            // Stack depth as word
                NULL,           // function parameter (like a generic object)
                1,              // Task Priority (Greater value has higher priority)
                &time_output_task_handle);  // Task handle

    if( xReturned_updateTask == pdPASS )
    {
        /* The task was created.  Use the task's handle to delete the task. */
        ESP_LOGI(TAG_RETREIVE, "time updater task started successfully");
        //vTaskDelete( xHandle );
    }

    if( xReturned_outputTask == pdPASS )
    {
        /* The task was created.  Use the task's handle to delete the task. */
        ESP_LOGI(TAG_RETREIVE, "time output task started successfully");
        //vTaskDelete( xHandle );
    }

}



/*
    ---------------------------------------------------------------------------------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------------------------------------------------------------------------------
    RETREIVAL & TIME UPDATE METHODS
    ---------------------------------------------------------------------------------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------------------------------------------------------------------------------
*/

/*
    ---------------------------------------------------------------------------------------------------------------------------------------------------------
    general
*/
/*
    request an update of the time with SNTP
        1. start wifi
        2. request update
        3. wait untill update completes
        4. stop wifi
*/
static void request_time_update(void)
{
    ESP_LOGI(TAG_RETREIVE, "retreiving time with SNTP protocol");

    start_wifi_connection();
    wait_until_wifi_connected();

    update_time_with_sntp();
    wait_until_time_updated();

    stop_wifi_connection();

}

/* initialize utilities */
static void initialize_utilities(void)
{
    ESP_LOGI(TAG_RETREIVE, "initializing utilities required for retreiving time with SNTP");
    initialize_non_volatile_storage();
    initialise_wifi();
}

/*
    ---------------------------------------------------------------------------------------------------------------------------------------------------------
    flash memory
*/
static void initialize_non_volatile_storage(void){
    ESP_LOGI(TAG_RETREIVE, "initializing non-volatile storage")
    ESP_ERROR_CHECK( nvs_flash_init() ); // initialize non-volatile storage
}

/*
    ---------------------------------------------------------------------------------------------------------------------------------------------------------
    SNTP - simple network time protocal
*/

/* request that time is updated with sntp service */
static void update_time_with_sntp(void)
{
    ESP_LOGI(TAG_RETREIVE, "requesting update of time with SNTP");

    ESP_LOGI(TAG_RETREIVE, "starting SNTP");
    sntp_setoperatingmode(SNTP_OPMODE_POLL); // set mode to listen only, we will manually poll every hour in a seperate thread
    sntp_setservername(0, "pool.ntp.org");
    sntp_init();
    ESP_LOGI(TAG_RETREIVE, "   SNTP polling opened. Waiting untill time updated...");
    wait_until_time_updated();
    ESP_LOGI(TAG_RETREIVE, "   time has been updated. closed SNTP polling.");
    sntp_stop();
    // sntp_stop

}
/* wait untill time has updated */
static void wait_until_time_updated(void)
{
    // wait for time to be set
    time_t now = 0;
    struct tm timeinfo = { 0 };
    int retry = 0;
    const int retry_count = 10;
    while(timeinfo.tm_year < (2016 - 1900) && ++retry < retry_count) {
        ESP_LOGI(TAG, "       Waiting for system time to be set... (%d/%d)", retry, retry_count);
        vTaskDelay(2000 / portTICK_PERIOD_MS);
        time(&now);
        localtime_r(&now, &timeinfo);
    }
}


/*
    ---------------------------------------------------------------------------------------------------------------------------------------------------------
    WiFi
    - https://esp-idf.readthedocs.io/en/latest/api-guides/wifi.html
*/

/*
    turn of wifi radio or turn on wifi radio - conserves power
    - ref : https://github.com/espressif/esp-idf/issues/1000
    - source:  https://github.com/espressif/esp-idf/blob/master/components/esp32/include/esp_wifi.h#L247
    - docs: https://esp-idf.readthedocs.io/en/latest/api-reference/wifi/esp_wifi.html
*/
static void start_wifi_connection(void)
{
    ESP_LOGI(TAG_RETREIVE, "starting WiFi radio and connection");
    ESP_ERROR_CHECK( esp_wifi_start() );
    ESP_ERROR_CHECK( esp_wifi_connect() );
}
static void stop_wifi_connection(void)
{
    ESP_LOGI(TAG_RETREIVE, "stopping WiFi radio and connection");
    ESP_ERROR_CHECK( esp_wifi_disconnect() );
    ESP_ERROR_CHECK( esp_wifi_stop() );
}
static void wait_until_wifi_connected(void){
    ESP_LOGI(TAG_RETREIVE, "waiting untill wifi has connected");
    xEventGroupWaitBits(wifi_event_group, CONNECTED_BIT, false, true, portMAX_DELAY); // waits untill wifi is connected
    ESP_LOGI(TAG_RETREIVE, "wifi is now connected");
}

/* initialize wifi object */
static void initialise_wifi(void)
{
    ESP_LOGI(TAG_RETREIVE, "initializing WIFI");
    tcpip_adapter_init();
    wifi_event_group = xEventGroupCreate();
    ESP_ERROR_CHECK( esp_event_loop_init(event_handler, NULL) );
    wifi_init_config_t cfg = WIFI_INIT_CONFIG_DEFAULT();
    ESP_ERROR_CHECK( esp_wifi_init(&cfg) );
    ESP_ERROR_CHECK( esp_wifi_set_storage(WIFI_STORAGE_RAM) );
    wifi_config_t wifi_config = {
        .sta = {
            .ssid = EXAMPLE_WIFI_SSID,
            .password = EXAMPLE_WIFI_PASS,
        },
    };
    ESP_LOGI(TAG_RETREIVE, "   Setting WiFi configuration SSID %s...", wifi_config.sta.ssid);
    ESP_ERROR_CHECK( esp_wifi_set_mode(WIFI_MODE_STA) );
    ESP_ERROR_CHECK( esp_wifi_set_config(ESP_IF_WIFI_STA, &wifi_config) );
    ESP_LOGI(TAG_RETREIVE, "    WIFI initialized successfully");
}
/* handle wifi error events */
static esp_err_t event_handler(void *ctx, system_event_t *event)
{
    switch(event->event_id) {
    case SYSTEM_EVENT_STA_START:
        esp_wifi_connect();
        break;
    case SYSTEM_EVENT_STA_GOT_IP:
        xEventGroupSetBits(wifi_event_group, CONNECTED_BIT);
        break;
    case SYSTEM_EVENT_STA_DISCONNECTED:
        /* This is a workaround as ESP32 WiFi libs don't currently
           auto-reassociate. */
        esp_wifi_connect();
        xEventGroupClearBits(wifi_event_group, CONNECTED_BIT);
        break;
    default:
        break;
    }
    return ESP_OK;
}
