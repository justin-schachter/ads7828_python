import ads7828

## Test throwing an address error exception: 
# adc = ads7828.ADS7828(0x89)

adc = ads7828.ADS7828(0x48)
print(adc._read_channel_single_ended_5())
while True:
    adc._self_test_single_ended_iref_on_ad_on()