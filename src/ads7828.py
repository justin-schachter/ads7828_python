###############################################################################
# Author: Justin Schachter (jschach@umich.edu)
###############################################################################
from enum import IntEnum
import smbus2 as smbus

###########################################################################
# ERROR CLASSES
###########################################################################
class AddressSelectionError(Exception):
    """
    Exception raised for errors in the input device address.

    Attributes:
        device  -- device class object
    """

    def __init__(self, device):
        self.address = device._device_addr
        list_of_available_addr_dec = [a.value for a in device.DeviceAddress]
        list_of_available_addr_hex = [hex(a.value) for a in device.DeviceAddress]
        self.message = f'Address selected for device ({self.address}) does'+\ 
                        'not match any of the available addresses (int):\n'+\
                       f'dec: {list_of_available_addr_dec}\n'+\
                       f'hex: {list_of_available_addr_hex}\n'    
        super().__init__(self.message)

class ADS7828():
    ###########################################################################
    # DATASHEET: https://www.ti.com/lit/ds/symlink/ads7828.pdf?ts=1638489227527
    ###########################################################################

    ###########################################################################
    # MEMBER VARIABLES
    ###########################################################################
    _device_addr = None                 #
    _command_byte = None                #
    _bit_res = 12                       #
    _voltage_reference = None           #
    _reference_warmup_time = None       #
    _millivolt_resolution = None        #
    _counts_to_voltage_transfer = None  #
    _single_ended_mode = True           #
    _average_window = None              #
    _average_dt = None                  #
    _i2c_bus_num = None                 #
    _i2c_bus = None                     #

    ###########################################################################
    # MEMBER CLASSES
    ###########################################################################
    class DeviceAddress(IntEnum):
        """
        This enum class defines the hardware addresses which correlate to pin
        states on the device. See datasheet page 11. 
        """
        #FORM: I2C_ADDR_A1_A0 WHERE:
        #   A1 = ADDRESS BIT 1 PIN STATE (1=HIGH/H, 0=LOW/L)
        #   A0 = ADDRESS BIT 0 PIN STATE (1=HIGH/H, 0=LOW/L)
        #   7-BIT ADDRESS: 0b[ 1 0 0 1 0 A1 A0 R/W ]
        #                     MSB              LSB
        I2C_ADDR_LL = 0x48
        I2C_ADDR_LH = 0x49
        I2C_ADDR_HL = 0x4A
        I2C_ADDR_HH = 0x4B
    
    class InputsRegister(IntEnum):
        """
        This register enum class defines the bits in the command byte that set
        the input mode as differential or single-ended for the measurement to 
        be conducted. Note that this needs to be configured for every read.
        """
        SINGLE_ENDED = 0x80
        DIFFERENTIAL = 0x00

    #TODO: UPDATE VALUES
    class SingleEndedChannelSelectionRegister(IntEnum):
        """
        This register enum class defines the bits in the command byte that set
        the channel selection for the measurement for single-ended measurements. 
        See datasheet page 11.
        """
        CH0 = 0x80
        CH1 = 0x80
        CH2 = 0x80
        CH3 = 0x80
        CH4 = 0x80
        CH5 = 0x80
        CH6 = 0x80
        CH7 = 0x80

    #TODO: UPDATE VALUES
    class DifferentialPositiveChannelSelectionRegister(IntEnum):
        """
        This register enum class defines the bits in the command byte that set
        the channel selection for the measurement for differential measurements
        where the lower channel number is the positive input. 
        See datasheet page 11.
        """
        # Polarity:   +   -
        DIFFERENTIAL_CH0_CH1 = 0x80
        DIFFERENTIAL_CH2_CH3 = 0x80
        DIFFERENTIAL_CH4_CH5 = 0x80
        DIFFERENTIAL_CH6_CH7 = 0x80

    #TODO: UPDATE VALUES
    class DifferentialNegativeChannelSelectionRegister(IntEnum):
        """
        This register enum class defines the bits in the command byte that set
        the channel selection for the measurement for differential measurements
        where the lower channel number is the positive input. 
        See datasheet page 11.
        """
        # Polarity:   +   -
        DIFFERENTIAL_CH1_CH0 = 0x80
        DIFFERENTIAL_CH3_CH2 = 0x80
        DIFFERENTIAL_CH5_CH4 = 0x80
        DIFFERENTIAL_CH7_CH6 = 0x80

    #TODO: UPDATE VALUES
    class PowerDownSelectionRegister(IntEnum):
        """
        This register enum class defines the bits in the command byte that set
        the power-down selection for the measurement. See datasheet page 11.
        """
        POWER_DOWN_BTWN_AD_CONVERSIONS = 0x80
        INTERNAL_REF_OFF_AD_ON         = 0x80
        INTERNAL_REF_ON_AD_OFF         = 0x80
        INTERNAL_REF_ON_AD_ON          = 0x80
    
    ###########################################################################
    # CONSTRUCTOR METHOD
    ###########################################################################
    def __init__(self, address=0x48, smbus_num=1):
        """
        Constructor.
        
        Parameters:
        address (int): Device address; must be one of the values in DeviceAddress (in hex/bin/dec)
        smbus_num (int): SMBus number being used on hardware; usually 0 or 1
        """
        #Set address and check if user set address is valid
        self._device_addr = address
        self.check_address()

        #Set defaults
        default_config()


    ###########################################################################
    # PUBLIC MEMBER METHODS (I.E. API METHODS)
    ###########################################################################
    def read_channel_single_ended(self, channel, 
                                  internal_ref_on=True, ad_on=True):
        """
        Communicates with the device to collect a single-ended measurement of a channel
        with input options for internal reference state and A/D converter state
    
        Parameters:
        channel (int): Channel number (0 to 7)
        internal_ref_on (bool): True means internal reference will be turned ON, False means OFF
        ad_on (bool): True means A/D converter will be turned ON, False means OFF
    
        Returns:
        int: voltage value (in volts, V) from selected channel
        """
        channel_names = [c.name for c in SingleEndedChannelSelectionRegister]
        


        return raw_voltage 
    


    ###########################################################################
    # PRIVATE MEMBER METHODS (I.E. API METHODS)
    ###########################################################################
    def _check_address(self):
        """
        Check if the current device address (I2C) is valid, else raise a error
        """
        list_of_available_addr = [addr.value for addr in self.DeviceAddress]
        if self._device_addr not in list_of_available_addr:
            raise AddressSelectionError(self)

    def _default_config(self):
        """
        Set all configuration variables 
        """
        #I2C Bus Setup --> defaults to Raspberry Pi default I2C bus number
        self._i2c_bus = smbus.SMBus(1)

        self._voltage_reference = 2.5 #internal reference voltage [V]

    def _read_channel_single_ended_0(self, internal_ref_on=True, ad_on=True):
        """
        [PRIVATE] Communicates with the device to collect a single-ended 
        measurement of a channel with input options for internal reference 
        state and A/D converter state
    
        Parameters:
        internal_ref_on (bool): True means internal reference will be turned ON, False means OFF
        ad_on (bool): True means A/D converter will be turned ON, False means OFF
    
        Returns:
        int: voltage value (in volts, V) from selected channel
        """
        channel_select = self.SingleEndedChannelSelectionRegister.CH0
        power_select_bits = _iref_and_ad_on_states(internal_ref_on,ad_on)
        self._command_byte = channel_select | power_select_bits

        return self._send_cmd_and_read_device()
    
    def _iref_and_ad_on_states(internal_ref_on, ad_on):
        """
        [PRIVATE] takes in a desired power state of the internal refence voltage and
        A/D converter and "ORs" them to produce a binary value that can be used to
        produce a device command byte via further bitwise operations.

        Parameters:
        internal_ref_on (bool): True means internal reference will be turned ON, False means OFF
        ad_on (bool): True means A/D converter will be turned ON, False means OFF
    
        Returns:
        int: binary result
        """
        INTERNAL_REF_ON_BIT = 0x08
        AD_CONVERTER_ON_BIT = 0x04
        #ternary logic operations based on input boolean values
        INTERNAL_REF_ON_BIT = 0x00 if not internal_ref_on else INTERNAL_REF_ON_BIT
        AD_CONVERTER_ON_BIT = 0x00 if not ad_on           else AD_CONVERTER_ON_BIT

        return INTERNAL_REF_ON_BIT | AD_CONVERTER_ON_BIT

    def _clear_command_byte_buffer(self)
        self._command_byte = None
        