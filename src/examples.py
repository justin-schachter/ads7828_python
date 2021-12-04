import ads7828
import math

## Test throwing an address error exception: 
# adc = ads7828.ADS7828(0x89)

adc = ads7828.ADS7828(0x48)

#Print a self test test with averaging
adc._self_test_single_ended_iref_on_ad_on()

#Print a self test test with averaging
adc._self_test_single_ended_iref_on_ad_on_averaged()

#print a new table of converted values: (these are the converted values for one of the Eddy EPS ADCs)
engineering_unit_ch0 = adc.read_channel_single_ended_averaged(0) / (0.005 * 100)            #I_5V0: I_LOAD = VOUT / (R_SENSE * GAIN)
engineering_unit_ch1 = adc.read_channel_single_ended_averaged(1) * ((100 + 33.2) / 33.2)    #V_5V0: V1 = V2 * ((R1+R2)/R2) [voltage divider]
engineering_unit_ch2 = adc.read_channel_single_ended_averaged(2) / (0.005 * 100)            #I_3V3: I_LOAD = VOUT / (R_SENSE * GAIN)
engineering_unit_ch3 = adc.read_channel_single_ended_averaged(3) * ((100 + 60.4) / 60.4)    #V_3V3: V1 = V2 * ((R1+R2)/R2) [voltage divider]
engineering_unit_ch4 = -1481.96 + math.sqrt(2.1962e6 + ((1.8639 - adc.read_channel_single_ended_averaged(4))/3.88e-6))  #LM20: See datasheet equation 3
engineering_unit_ch5 = adc.read_channel_single_ended_averaged(5) * ((100 + 12) / 12)        #V_VBATT_RAW: V1 = V2 * ((R1+R2)/R2) [voltage divider]
engineering_unit_ch6 = adc.read_channel_single_ended_averaged(6) / (0.012 * 100)            #I_VBATT_RAW: I_LOAD = VOUT / (R_SENSE * GAIN)
engineering_unit_ch7 = -1481.96 + math.sqrt(2.1962e6 + ((1.8639 - adc.read_channel_single_ended_averaged(7))/3.88e-6))
