import ads7828

## Test throwing an address error exception: 
# adc_0 = ads7828.ADS7828(0x89)

adc_0 = ads7828.ADS7828(0x48)

while True:
    adc_0._self_test_single_ended_iref_on_ad_on()