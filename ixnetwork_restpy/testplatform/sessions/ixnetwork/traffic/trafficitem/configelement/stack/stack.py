# MIT LICENSE
#
# Copyright 1997 - 2020 by IXIA Keysight
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE. 
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Stack(Base):
    """This object helps to specify the field properties of a protocol stack.
    The Stack class encapsulates a list of stack resources that are managed by the system.
    A list of resources can be retrieved from the server using the Stack.find() method.
    """

    __slots__ = '_stack_index'
    _SDM_NAME = 'stack'
    _SDM_ATT_MAP = {
        'DisplayName': 'displayName',
        'StackTypeId': 'stackTypeId',
        'TemplateName': 'templateName',
    }

    def __init__(self, parent):
        super(Stack, self).__init__(parent)
        self._stack_index = 0

    @property
    def Field(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.field.field.Field): An instance of the Field class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.field.field import Field
        if self._properties.get('Field', None) is None:
            return Field(self)
        else:
            return self._properties.get('Field')

    @property
    def IxP4_MPLS(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ixP4_MPLS_template import IxP4_MPLS
        return IxP4_MPLS(self)

    @property
    def IxP4_P4CALC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ixP4_P4CALC_template import IxP4_P4CALC
        return IxP4_P4CALC(self)

    @property
    def IxP4_ETHERNET(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ixP4_ETHERNET_template import IxP4_ETHERNET
        return IxP4_ETHERNET(self)

    @property
    def IxP4_ETHERNET_without_FCS(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ixP4_ETHERNETwithoutFCS_template import IxP4_ETHERNET_without_FCS
        return IxP4_ETHERNET_without_FCS(self)

    @property
    def IEC_61883_4_Source_Packet(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.sourcePacketHeader_template import IEC_61883_4_Source_Packet
        return IEC_61883_4_Source_Packet(self)

    @property
    def IEC_61883_6_24_Bit_Data(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.iec61883_6_24_BitData_template import IEC_61883_6_24_Bit_Data
        return IEC_61883_6_24_Bit_Data(self)

    @property
    def RTCP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.realTimeTransportControlProtocol_template import RTCP
        return RTCP(self)

    @property
    def IEC_61883_1(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.iec61883_1_template import IEC_61883_1
        return IEC_61883_1(self)

    @property
    def H264_CSRC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.h264_csrc_template import H264_CSRC
        return H264_CSRC(self)

    @property
    def H264_Specific_Header(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.h264_sh_template import H264_Specific_Header
        return H264_Specific_Header(self)

    @property
    def AVTP_17221(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.avtpdu_template import AVTP_17221
        return AVTP_17221(self)

    @property
    def H264(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.h264_template import H264
        return H264(self)

    @property
    def JPEG_2000_Video_Format(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.jpeg2000VideoFormat_template import JPEG_2000_Video_Format
        return JPEG_2000_Video_Format(self)

    @property
    def JPEG_Video_Format(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.jpegVideoFormat_template import JPEG_Video_Format
        return JPEG_Video_Format(self)

    @property
    def SDI_Video_Format(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.sdiVideoFormat_template import SDI_Video_Format
        return SDI_Video_Format(self)

    @property
    def MPEG2TS_Payload(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mpegtsPayload_template import MPEG2TS_Payload
        return MPEG2TS_Payload(self)

    @property
    def MMA_Data_Payload(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mmaDataPayload_template import MMA_Data_Payload
        return MMA_Data_Payload(self)

    @property
    def G723_Sid_Mode(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.G723SidMode_template import G723_Sid_Mode
        return G723_Sid_Mode(self)

    @property
    def G723_Frame_Packing(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.G723Framepacking_template import G723_Frame_Packing
        return G723_Frame_Packing(self)

    @property
    def G723_Frame_Packing_53(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.G723Framepacking53_template import G723_Frame_Packing_53
        return G723_Frame_Packing_53(self)

    @property
    def CN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.CN_template import CN
        return CN(self)

    @property
    def RTCP_1733(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.realTimeTransportControlProtocol1733_template import RTCP_1733
        return RTCP_1733(self)

    @property
    def AAL5(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.aal5_template import AAL5
        return AAL5(self)

    @property
    def ATM_Cell(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.atmCell_template import ATM_Cell
        return ATM_Cell(self)

    @property
    def Atm_Aal5_Frame(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.atmAAL5Frame_template import Atm_Aal5_Frame
        return Atm_Aal5_Frame(self)

    @property
    def Ethernet_ARP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ethernetARP_template import Ethernet_ARP
        return Ethernet_ARP(self)

    @property
    def Cisco_HDLC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ciscoHDLC_template import Cisco_HDLC
        return Cisco_HDLC(self)

    @property
    def Cisco_ISL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ciscoISL_template import Cisco_ISL
        return Cisco_ISL(self)

    @property
    def Cisco_Frame_Relay(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ciscoFrameRelay_template import Cisco_Frame_Relay
        return Cisco_Frame_Relay(self)

    @property
    def Ethernet_II(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ethernet_template import Ethernet_II
        return Ethernet_II(self)

    @property
    def Ethernet_II_without_FCS(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ethernetNoFCS_template import Ethernet_II_without_FCS
        return Ethernet_II_without_FCS(self)

    @property
    def Frame_Relay(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.frameRelay_template import Frame_Relay
        return Frame_Relay(self)

    @property
    def PPP_IPCP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pppIPCP_template import PPP_IPCP
        return PPP_IPCP(self)

    @property
    def PPP_IPV6CP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pppIPv6CP_template import PPP_IPV6CP
        return PPP_IPV6CP(self)

    @property
    def LACP_with_Ethernet(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lacp_template import LACP_with_Ethernet
        return LACP_with_Ethernet(self)

    @property
    def LACP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lacpWithoutEthernet_template import LACP
        return LACP(self)

    @property
    def LLC_PPP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.llcPPP_template import LLC_PPP
        return LLC_PPP(self)

    @property
    def Connectivity_Fault_Management_CFM(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.cfm_template import Connectivity_Fault_Management_CFM
        return Connectivity_Fault_Management_CFM(self)

    @property
    def Link_OAM(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.linkOAM_template import Link_OAM
        return Link_OAM(self)

    @property
    def E_LMI(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.elmi_template import E_LMI
        return E_LMI(self)

    @property
    def LLC_Bridged_Ethernet_8023(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.llcBridgedEthernet_template import LLC_Bridged_Ethernet_8023
        return LLC_Bridged_Ethernet_8023(self)

    @property
    def LLC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.llc_template import LLC
        return LLC(self)

    @property
    def L2VPN_ATM_Cell_CW(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNATMCellCW_template import L2VPN_ATM_Cell_CW
        return L2VPN_ATM_Cell_CW(self)

    @property
    def L2VPN_ATM_CW_Frame(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNATMCWFrame_template import L2VPN_ATM_CW_Frame
        return L2VPN_ATM_CW_Frame(self)

    @property
    def L2VPN_Ethernet_Frame(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNEthernetFrame_template import L2VPN_Ethernet_Frame
        return L2VPN_Ethernet_Frame(self)

    @property
    def L2VPN_FR_CW(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNFrameRelayCW_template import L2VPN_FR_CW
        return L2VPN_FR_CW(self)

    @property
    def L2VPN_FR_RFC4619_CW(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNFrameRelayRFC4619CW_template import L2VPN_FR_RFC4619_CW
        return L2VPN_FR_RFC4619_CW(self)

    @property
    def L2VPN_FR(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNFrameRelay_template import L2VPN_FR
        return L2VPN_FR(self)

    @property
    def L2VPN_PPP_HDLC_Frame(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNPPPHDLC_template import L2VPN_PPP_HDLC_Frame
        return L2VPN_PPP_HDLC_Frame(self)

    @property
    def L2VPN_HDLC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNHDLC_template import L2VPN_HDLC
        return L2VPN_HDLC(self)

    @property
    def L2VPN_PPP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNPPP_template import L2VPN_PPP
        return L2VPN_PPP(self)

    @property
    def L2VPN_VC_Type_IP_CW(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2VPNVCTypeIPCW_template import L2VPN_VC_Type_IP_CW
        return L2VPN_VC_Type_IP_CW(self)

    @property
    def MAC_in_MAC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.macInMAC_template import MAC_in_MAC
        return MAC_in_MAC(self)

    @property
    def MAC_in_MAC_No_FCS(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.macInMACNoFcs_template import MAC_in_MAC_No_FCS
        return MAC_in_MAC_No_FCS(self)

    @property
    def Marker_PDU(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.markerPDU_template import Marker_PDU
        return Marker_PDU(self)

    @property
    def MPLS(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mpls_enull_template import MPLS
        return MPLS(self)

    @property
    def MSTP_BPDU(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mstpBPDU_template import MSTP_BPDU
        return MSTP_BPDU(self)

    @property
    def MPLS_TP_Ethernet_Frame(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.MPLSTPEthernetFrame_template import MPLS_TP_Ethernet_Frame
        return MPLS_TP_Ethernet_Frame(self)

    @property
    def OAM_Depricated(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.oamCCM_template import OAM_Depricated
        return OAM_Depricated(self)

    @property
    def PPP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ppp_template import PPP
        return PPP(self)

    @property
    def PPP_without_HDLC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pppWithoutHDLC_template import PPP_without_HDLC
        return PPP_without_HDLC(self)

    @property
    def PPP_LCP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pppLCP_template import PPP_LCP
        return PPP_LCP(self)

    @property
    def PPP_PAP_CHAP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pppPAPCHAP_template import PPP_PAP_CHAP
        return PPP_PAP_CHAP(self)

    @property
    def PPPoE___Discovery(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pppoEDiscovery_template import PPPoE___Discovery
        return PPPoE___Discovery(self)

    @property
    def PPPoE___Session(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pppoESession_template import PPPoE___Session
        return PPPoE___Session(self)

    @property
    def PTPv2(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.PTPv2_template import PTPv2
        return PTPv2(self)

    @property
    def Ethernet_RARP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ethernetRARP_template import Ethernet_RARP
        return Ethernet_RARP(self)

    @property
    def RSTP_BPDU(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.rstpBPDU_template import RSTP_BPDU
        return RSTP_BPDU(self)

    @property
    def LLC_SNAP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.llcSNAP_template import LLC_SNAP
        return LLC_SNAP(self)

    @property
    def SNAP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.snap_template import SNAP
        return SNAP(self)

    @property
    def STP_Configuration_BPDU(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.stpCfgBPDU_template import STP_Configuration_BPDU
        return STP_Configuration_BPDU(self)

    @property
    def STP_TCN_BPDU(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.stpTCNBPDU_template import STP_TCN_BPDU
        return STP_TCN_BPDU(self)

    @property
    def Virtual_Circuit_Multiplexed_Bridged_Ethernet_8023(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.vcMuxBridgedEthernet_template import Virtual_Circuit_Multiplexed_Bridged_Ethernet_8023
        return Virtual_Circuit_Multiplexed_Bridged_Ethernet_8023(self)

    @property
    def VCMux_PPP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.vcMuxPPP_template import VCMux_PPP
        return VCMux_PPP(self)

    @property
    def VLAN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.vlan_template import VLAN
        return VLAN(self)

    @property
    def VNTAG(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.vntag_template import VNTAG
        return VNTAG(self)

    @property
    def VIC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.vic_template import VIC
        return VIC(self)

    @property
    def VPLS_Ethernet_Frame(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.vplsEthernet_template import VPLS_Ethernet_Frame
        return VPLS_Ethernet_Frame(self)

    @property
    def FCoE(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcoE_template import FCoE
        return FCoE(self)

    @property
    def FCoE_Fabric_LOGO(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEFabricLogoEnode_template import FCoE_Fabric_LOGO
        return FCoE_Fabric_LOGO(self)

    @property
    def FCoE_Fabric_LOGO_LS_ACC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEFabricLogoLsAcc_template import FCoE_Fabric_LOGO_LS_ACC
        return FCoE_Fabric_LOGO_LS_ACC(self)

    @property
    def FCoE_Fabric_LOGO_LS_RJT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEFabricLogoLsRjt_template import FCoE_Fabric_LOGO_LS_RJT
        return FCoE_Fabric_LOGO_LS_RJT(self)

    @property
    def FCoE_FLOGI_LS_ACC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEFlogiLsAcc_template import FCoE_FLOGI_LS_ACC
        return FCoE_FLOGI_LS_ACC(self)

    @property
    def FCoE_FLOGI_LS_RJT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEFlogiLsRjt_template import FCoE_FLOGI_LS_RJT
        return FCoE_FLOGI_LS_RJT(self)

    @property
    def FCoE_FLOGI_Request(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEFlogiRequest_template import FCoE_FLOGI_Request
        return FCoE_FLOGI_Request(self)

    @property
    def FCoE_PLOGI_LS_ACC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEPlogiLsAcc_template import FCoE_PLOGI_LS_ACC
        return FCoE_PLOGI_LS_ACC(self)

    @property
    def FCoE_PLOGI_LS_RJT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEPlogiLsRjt_template import FCoE_PLOGI_LS_RJT
        return FCoE_PLOGI_LS_RJT(self)

    @property
    def FCoE_PLOGI_Request(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEPlogiRequest_template import FCoE_PLOGI_Request
        return FCoE_PLOGI_Request(self)

    @property
    def FCoE_NPIV_FDISC_LS_ACC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoENpivFdicsLsAcc_template import FCoE_NPIV_FDISC_LS_ACC
        return FCoE_NPIV_FDISC_LS_ACC(self)

    @property
    def FCoE_NPIV_FDISC_LS_RJT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoENpivFdiscLsRjt_template import FCoE_NPIV_FDISC_LS_RJT
        return FCoE_NPIV_FDISC_LS_RJT(self)

    @property
    def FCoE_NPIV_FDISC_Request(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoENpivFdiscRequest_template import FCoE_NPIV_FDISC_Request
        return FCoE_NPIV_FDISC_Request(self)

    @property
    def FCoE_RSCN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERscn_template import FCoE_RSCN
        return FCoE_RSCN(self)

    @property
    def FCoE_SCR_Request(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEScrRequest_template import FCoE_SCR_Request
        return FCoE_SCR_Request(self)

    @property
    def FCoE_GCS_ID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGCSID_template import FCoE_GCS_ID
        return FCoE_GCS_ID(self)

    @property
    def FCoE_GA_NXT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGANXT_template import FCoE_GA_NXT
        return FCoE_GA_NXT(self)

    @property
    def FCoE_GIEIL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGIEIL_template import FCoE_GIEIL
        return FCoE_GIEIL(self)

    @property
    def FCoE_GID_PN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGIDPN_template import FCoE_GID_PN
        return FCoE_GID_PN(self)

    @property
    def FCoE_GFPN_ID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGFPNID_template import FCoE_GFPN_ID
        return FCoE_GFPN_ID(self)

    @property
    def FCoE_GPSC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPSC_template import FCoE_GPSC
        return FCoE_GPSC(self)

    @property
    def FCoE_GSES(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGSES_template import FCoE_GSES
        return FCoE_GSES(self)

    @property
    def FCoE_GPN_FT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPNFT_template import FCoE_GPN_FT
        return FCoE_GPN_FT(self)

    @property
    def FCoE_GIEILN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGIEILN_template import FCoE_GIEILN
        return FCoE_GIEILN(self)

    @property
    def FCoE_GAPNL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGAPNL_template import FCoE_GAPNL
        return FCoE_GAPNL(self)

    @property
    def FCoE_GSPN_ID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGSPNID_template import FCoE_GSPN_ID
        return FCoE_GSPN_ID(self)

    @property
    def FCoE_RSNN_NN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERSNNNN_template import FCoE_RSNN_NN
        return FCoE_RSNN_NN(self)

    @property
    def FCoE_GNPL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGNPL_template import FCoE_GNPL
        return FCoE_GNPL(self)

    @property
    def FCoE_GPL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPL_template import FCoE_GPL
        return FCoE_GPL(self)

    @property
    def FCoE_GNID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGNID_template import FCoE_GNID
        return FCoE_GNID(self)

    @property
    def FCoE_RPLT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERPLT_template import FCoE_RPLT
        return FCoE_RPLT(self)

    @property
    def FCoE_RIELN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERIELN_template import FCoE_RIELN
        return FCoE_RIELN(self)

    @property
    def FCoE_GPNL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPNL_template import FCoE_GPNL
        return FCoE_GPNL(self)

    @property
    def FCoE_GNN_FT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGNNFT_template import FCoE_GNN_FT
        return FCoE_GNN_FT(self)

    @property
    def FCoE_GPLNL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPLNL_template import FCoE_GPLNL
        return FCoE_GPLNL(self)

    @property
    def FCoE_RFT_ID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERFTID_template import FCoE_RFT_ID
        return FCoE_RFT_ID(self)

    @property
    def FCoE_GPLML(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPLML_template import FCoE_GPLML
        return FCoE_GPLML(self)

    @property
    def FCoE_GPS(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPS_template import FCoE_GPS
        return FCoE_GPS(self)

    @property
    def FCoE_RCS_ID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERCSID_template import FCoE_RCS_ID
        return FCoE_RCS_ID(self)

    @property
    def FCoE_GSNN_NN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGSNNNN_template import FCoE_GSNN_NN
        return FCoE_GSNN_NN(self)

    @property
    def FCoE_GNN_ID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGNNID_template import FCoE_GNN_ID
        return FCoE_GNN_ID(self)

    @property
    def FCoE_GMID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGMID_template import FCoE_GMID
        return FCoE_GMID(self)

    @property
    def FCoE_GIET(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGIET_template import FCoE_GIET
        return FCoE_GIET(self)

    @property
    def FCoE_RPLM(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERPLM_template import FCoE_RPLM
        return FCoE_RPLM(self)

    @property
    def FCoE_GPAB(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPAB_template import FCoE_GPAB
        return FCoE_GPAB(self)

    @property
    def FCoE_GIEAG(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGIEAG_template import FCoE_GIEAG
        return FCoE_GIEAG(self)

    @property
    def FCoE_GIEL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGIEL_template import FCoE_GIEL
        return FCoE_GIEL(self)

    @property
    def FCoE_GPAG(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPAG_template import FCoE_GPAG
        return FCoE_GPAG(self)

    @property
    def FCoE_GID_FT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGIDFT_template import FCoE_GID_FT
        return FCoE_GID_FT(self)

    @property
    def FCoE_GFF_ID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGFFID_template import FCoE_GFF_ID
        return FCoE_GFF_ID(self)

    @property
    def FCoE_GMAL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGMAL_template import FCoE_GMAL
        return FCoE_GMAL(self)

    @property
    def FCoE_GPT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPT_template import FCoE_GPT
        return FCoE_GPT(self)

    @property
    def FCoE_GPT_ID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPTID_template import FCoE_GPT_ID
        return FCoE_GPT_ID(self)

    @property
    def FCoE_GATIN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGATIN_template import FCoE_GATIN
        return FCoE_GATIN(self)

    @property
    def FCoE_RFF_ID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERFFID_template import FCoE_RFF_ID
        return FCoE_RFF_ID(self)

    @property
    def FCoE_RPNL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERPNL_template import FCoE_RPNL
        return FCoE_RPNL(self)

    @property
    def FCoE_GDID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGDID_template import FCoE_GDID
        return FCoE_GDID(self)

    @property
    def FCoE_GTIN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGTIN_template import FCoE_GTIN
        return FCoE_GTIN(self)

    @property
    def FCoE_RPL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERPL_template import FCoE_RPL
        return FCoE_RPL(self)

    @property
    def FCoE_GPLT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPLT_template import FCoE_GPLT
        return FCoE_GPLT(self)

    @property
    def FCoE_RNN_ID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERNNID_template import FCoE_RNN_ID
        return FCoE_RNN_ID(self)

    @property
    def FCoE_GPPN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPPN_template import FCoE_GPPN
        return FCoE_GPPN(self)

    @property
    def FCoE_GPFCP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPFCP_template import FCoE_GPFCP
        return FCoE_GPFCP(self)

    @property
    def FCoE_GPLI(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPLI_template import FCoE_GPLI
        return FCoE_GPLI(self)

    @property
    def FCoE_GFN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGFN_template import FCoE_GFN
        return FCoE_GFN(self)

    @property
    def FCoE_RPAB(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERPAB_template import FCoE_RPAB
        return FCoE_RPAB(self)

    @property
    def FCoE_GFT_ID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGFTID_template import FCoE_GFT_ID
        return FCoE_GFT_ID(self)

    @property
    def FCoE_RSPN_ID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERSPNID_template import FCoE_RSPN_ID
        return FCoE_RSPN_ID(self)

    @property
    def FCoE_GID_NN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGIDNN_template import FCoE_GID_NN
        return FCoE_GID_NN(self)

    @property
    def FCoE_GPN_ID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEGPNID_template import FCoE_GPN_ID
        return FCoE_GPN_ID(self)

    @property
    def FCoE_EFP_SW_RJT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEEFPSWRJT_template import FCoE_EFP_SW_RJT
        return FCoE_EFP_SW_RJT(self)

    @property
    def FCoE_EFP_SW_ACC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEEFPSWACC_template import FCoE_EFP_SW_ACC
        return FCoE_EFP_SW_ACC(self)

    @property
    def FCoE_ESC_SW_ACC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEESCSWACC_template import FCoE_ESC_SW_ACC
        return FCoE_ESC_SW_ACC(self)

    @property
    def FCoE_RDI_SW_RJT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERDISWRJT_template import FCoE_RDI_SW_RJT
        return FCoE_RDI_SW_RJT(self)

    @property
    def FCoE_MR_Request(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEMRRequest_template import FCoE_MR_Request
        return FCoE_MR_Request(self)

    @property
    def FCoE_LSA_Request(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoELSARequest_template import FCoE_LSA_Request
        return FCoE_LSA_Request(self)

    @property
    def FCoE_DIA_SW_RJT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEDIASWRJT_template import FCoE_DIA_SW_RJT
        return FCoE_DIA_SW_RJT(self)

    @property
    def FCoE_MR_SW_RJT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEMRSWRJT_template import FCoE_MR_SW_RJT
        return FCoE_MR_SW_RJT(self)

    @property
    def FCoE_DIA_SW_ACC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEDIASWACC_template import FCoE_DIA_SW_ACC
        return FCoE_DIA_SW_ACC(self)

    @property
    def FCoE_RDI_SW_ACC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERDISWACC_template import FCoE_RDI_SW_ACC
        return FCoE_RDI_SW_ACC(self)

    @property
    def FCoE_ESC_SW_RJT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEESCSWRJT_template import FCoE_ESC_SW_RJT
        return FCoE_ESC_SW_RJT(self)

    @property
    def FCoE_LSU_Request(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoELSURequest_template import FCoE_LSU_Request
        return FCoE_LSU_Request(self)

    @property
    def FCoE_ESC_Request(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEESCRequest_template import FCoE_ESC_Request
        return FCoE_ESC_Request(self)

    @property
    def FCoE_ELP_SW_ACC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEELPSWACC_template import FCoE_ELP_SW_ACC
        return FCoE_ELP_SW_ACC(self)

    @property
    def FCoE_ELP_SW_RJT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEELPSWRJT_template import FCoE_ELP_SW_RJT
        return FCoE_ELP_SW_RJT(self)

    @property
    def FCoE_MR_SW_ACC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEMRSWACC_template import FCoE_MR_SW_ACC
        return FCoE_MR_SW_ACC(self)

    @property
    def FCoE_ELP_Request(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEELPRequest_template import FCoE_ELP_Request
        return FCoE_ELP_Request(self)

    @property
    def FCoE_DIA_Request(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEDIARequest_template import FCoE_DIA_Request
        return FCoE_DIA_Request(self)

    @property
    def FCoE_RDI_Request(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoERDIRequest_template import FCoE_RDI_Request
        return FCoE_RDI_Request(self)

    @property
    def FCoE_HLO_Request(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEHLORequest_template import FCoE_HLO_Request
        return FCoE_HLO_Request(self)

    @property
    def FCoE_EFP_Request(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fCoEEFPRequest_template import FCoE_EFP_Request
        return FCoE_EFP_Request(self)

    @property
    def FIP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fip_template import FIP
        return FIP(self)

    @property
    def FIP_Clear_Virtual_Links_FCF(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipClearVirtualLinksFcf_template import FIP_Clear_Virtual_Links_FCF
        return FIP_Clear_Virtual_Links_FCF(self)

    @property
    def FIP_Discovery_Advertisement_FCF(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipDiscoveryAdvertisementFcf_template import FIP_Discovery_Advertisement_FCF
        return FIP_Discovery_Advertisement_FCF(self)

    @property
    def FIP_Discovery_Solicitation_ENode(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipDiscoverySolicitationEnode_template import FIP_Discovery_Solicitation_ENode
        return FIP_Discovery_Solicitation_ENode(self)

    @property
    def FIP_Discovery_Solicitation_FCF(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipDiscoverySolicitationFcf_template import FIP_Discovery_Solicitation_FCF
        return FIP_Discovery_Solicitation_FCF(self)

    @property
    def FIP_ELP_Request_FCF(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipElpRequestFcf_template import FIP_ELP_Request_FCF
        return FIP_ELP_Request_FCF(self)

    @property
    def FIP_ELP_SW_ACC_FCF(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipElpSwAccFcf_template import FIP_ELP_SW_ACC_FCF
        return FIP_ELP_SW_ACC_FCF(self)

    @property
    def FIP_ELP_SW_RJT_FCF(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipElpSwRjtFcf_template import FIP_ELP_SW_RJT_FCF
        return FIP_ELP_SW_RJT_FCF(self)

    @property
    def FIP_Fabric_LOGO_ENode(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipFabricLogoEnode_template import FIP_Fabric_LOGO_ENode
        return FIP_Fabric_LOGO_ENode(self)

    @property
    def FIP_Fabric_LOGO_LS_ACC_FCF(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipFabricLogoLsAccFcf_template import FIP_Fabric_LOGO_LS_ACC_FCF
        return FIP_Fabric_LOGO_LS_ACC_FCF(self)

    @property
    def FIP_Fabric_LOGO_LS_RJT_FCF(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipFabricLogoLsRjtFcf_template import FIP_Fabric_LOGO_LS_RJT_FCF
        return FIP_Fabric_LOGO_LS_RJT_FCF(self)

    @property
    def FIP_FLOGI_LS_ACC_FCF(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipFlogiLsAccFcf_template import FIP_FLOGI_LS_ACC_FCF
        return FIP_FLOGI_LS_ACC_FCF(self)

    @property
    def FIP_FLOGI_LS_RJT_FCF(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipFlogiLsRjtFcf_template import FIP_FLOGI_LS_RJT_FCF
        return FIP_FLOGI_LS_RJT_FCF(self)

    @property
    def FIP_FLOGI_Request_ENode(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipFlogiRequestEnode_template import FIP_FLOGI_Request_ENode
        return FIP_FLOGI_Request_ENode(self)

    @property
    def FIP_Keep_Alive_ENode(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipKeepAliveEnode_template import FIP_Keep_Alive_ENode
        return FIP_Keep_Alive_ENode(self)

    @property
    def FIP_Keep_Alive_VN_Port(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipKeepAliveVnport_template import FIP_Keep_Alive_VN_Port
        return FIP_Keep_Alive_VN_Port(self)

    @property
    def FIP_NPIV_FDISC_LS_ACC_FCF(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipNpivFdicsLsAccFcf_template import FIP_NPIV_FDISC_LS_ACC_FCF
        return FIP_NPIV_FDISC_LS_ACC_FCF(self)

    @property
    def FIP_NPIV_FDISC_LS_RJT_FCF(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipNpivFdiscLsRjtFcf_template import FIP_NPIV_FDISC_LS_RJT_FCF
        return FIP_NPIV_FDISC_LS_RJT_FCF(self)

    @property
    def FIP_NPIV_FDISC_Request_ENode(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipNpivFdiscRequestEnode_template import FIP_NPIV_FDISC_Request_ENode
        return FIP_NPIV_FDISC_Request_ENode(self)

    @property
    def FIP_Vendor_Specific(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipVendorSpecific_template import FIP_Vendor_Specific
        return FIP_Vendor_Specific(self)

    @property
    def FIP_VLAN_Notification_FCF(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipVlanNotificationFcf_template import FIP_VLAN_Notification_FCF
        return FIP_VLAN_Notification_FCF(self)

    @property
    def FIP_VLAN_Request(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fipVlanRequest_template import FIP_VLAN_Request
        return FIP_VLAN_Request(self)

    @property
    def FC_Fabric_LOGO(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcFabricLogoEnode_template import FC_Fabric_LOGO
        return FC_Fabric_LOGO(self)

    @property
    def FC_Fabric_LOGO_LS_ACC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcFabricLogoLsAcc_template import FC_Fabric_LOGO_LS_ACC
        return FC_Fabric_LOGO_LS_ACC(self)

    @property
    def FC_Fabric_LOGO_LS_RJT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcFabricLogoLsRjt_template import FC_Fabric_LOGO_LS_RJT
        return FC_Fabric_LOGO_LS_RJT(self)

    @property
    def FC_FLOGI_LS_ACC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcFlogiLsAcc_template import FC_FLOGI_LS_ACC
        return FC_FLOGI_LS_ACC(self)

    @property
    def FC_FLOGI_LS_RJT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcFlogiLsRjt_template import FC_FLOGI_LS_RJT
        return FC_FLOGI_LS_RJT(self)

    @property
    def FC_FLOGI_Request(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcFlogiRequest_template import FC_FLOGI_Request
        return FC_FLOGI_Request(self)

    @property
    def FC_PLOGI_LS_ACC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcPlogiLsAcc_template import FC_PLOGI_LS_ACC
        return FC_PLOGI_LS_ACC(self)

    @property
    def FC_PLOGI_LS_RJT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcPlogiLsRjt_template import FC_PLOGI_LS_RJT
        return FC_PLOGI_LS_RJT(self)

    @property
    def FC_PLOGI_Request(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcPlogiRequest_template import FC_PLOGI_Request
        return FC_PLOGI_Request(self)

    @property
    def FC_NPIV_FDISC_LS_ACC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcNpivFdicsLsAcc_template import FC_NPIV_FDISC_LS_ACC
        return FC_NPIV_FDISC_LS_ACC(self)

    @property
    def FC_NPIV_FDISC_LS_RJT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcNpivFdiscLsRjt_template import FC_NPIV_FDISC_LS_RJT
        return FC_NPIV_FDISC_LS_RJT(self)

    @property
    def FC_NPIV_FDISC_Request(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcNpivFdiscRequest_template import FC_NPIV_FDISC_Request
        return FC_NPIV_FDISC_Request(self)

    @property
    def FC_SCR_Request(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcScrRequest_template import FC_SCR_Request
        return FC_SCR_Request(self)

    @property
    def FC_RSCN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fcRscn_template import FC_RSCN
        return FC_RSCN(self)

    @property
    def FC_GCS_ID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGCSID_template import FC_GCS_ID
        return FC_GCS_ID(self)

    @property
    def FC_GA_NXT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGANXT_template import FC_GA_NXT
        return FC_GA_NXT(self)

    @property
    def FC_GIEIL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGIEIL_template import FC_GIEIL
        return FC_GIEIL(self)

    @property
    def FC_GID_PN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGIDPN_template import FC_GID_PN
        return FC_GID_PN(self)

    @property
    def FC_GFPN_ID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGFPNID_template import FC_GFPN_ID
        return FC_GFPN_ID(self)

    @property
    def FC_GPSC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGPSC_template import FC_GPSC
        return FC_GPSC(self)

    @property
    def FC_GSES(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGSES_template import FC_GSES
        return FC_GSES(self)

    @property
    def FC_GPN_FT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGPNFT_template import FC_GPN_FT
        return FC_GPN_FT(self)

    @property
    def FC_GIEILN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGIEILN_template import FC_GIEILN
        return FC_GIEILN(self)

    @property
    def FC_GAPNL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGAPNL_template import FC_GAPNL
        return FC_GAPNL(self)

    @property
    def FC_GSPN_ID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGSPNID_template import FC_GSPN_ID
        return FC_GSPN_ID(self)

    @property
    def FC_RSNN_NN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCRSNNNN_template import FC_RSNN_NN
        return FC_RSNN_NN(self)

    @property
    def FC_GNPL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGNPL_template import FC_GNPL
        return FC_GNPL(self)

    @property
    def FC_GPL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGPL_template import FC_GPL
        return FC_GPL(self)

    @property
    def FC_GNID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGNID_template import FC_GNID
        return FC_GNID(self)

    @property
    def FC_RPLT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCRPLT_template import FC_RPLT
        return FC_RPLT(self)

    @property
    def FC_RIELN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCRIELN_template import FC_RIELN
        return FC_RIELN(self)

    @property
    def FC_GPNL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGPNL_template import FC_GPNL
        return FC_GPNL(self)

    @property
    def FC_GNN_FT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGNNFT_template import FC_GNN_FT
        return FC_GNN_FT(self)

    @property
    def FC_GPLNL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGPLNL_template import FC_GPLNL
        return FC_GPLNL(self)

    @property
    def FC_RFT_ID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCRFTID_template import FC_RFT_ID
        return FC_RFT_ID(self)

    @property
    def FC_GPLML(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGPLML_template import FC_GPLML
        return FC_GPLML(self)

    @property
    def FC_GPS(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGPS_template import FC_GPS
        return FC_GPS(self)

    @property
    def FC_RCS_ID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCRCSID_template import FC_RCS_ID
        return FC_RCS_ID(self)

    @property
    def FC_GSNN_NN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGSNNNN_template import FC_GSNN_NN
        return FC_GSNN_NN(self)

    @property
    def FC_GNN_ID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGNNID_template import FC_GNN_ID
        return FC_GNN_ID(self)

    @property
    def FC_GMID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGMID_template import FC_GMID
        return FC_GMID(self)

    @property
    def FC_GIET(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGIET_template import FC_GIET
        return FC_GIET(self)

    @property
    def FC_RPLM(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCRPLM_template import FC_RPLM
        return FC_RPLM(self)

    @property
    def FC_GPAB(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGPAB_template import FC_GPAB
        return FC_GPAB(self)

    @property
    def FC_GIEAG(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGIEAG_template import FC_GIEAG
        return FC_GIEAG(self)

    @property
    def FC_GIEL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGIEL_template import FC_GIEL
        return FC_GIEL(self)

    @property
    def FC_GPAG(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGPAG_template import FC_GPAG
        return FC_GPAG(self)

    @property
    def FC_GID_FT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGIDFT_template import FC_GID_FT
        return FC_GID_FT(self)

    @property
    def FC_GFF_ID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGFFID_template import FC_GFF_ID
        return FC_GFF_ID(self)

    @property
    def FC_GMAL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGMAL_template import FC_GMAL
        return FC_GMAL(self)

    @property
    def FC_GPT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGPT_template import FC_GPT
        return FC_GPT(self)

    @property
    def FC_GPT_ID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGPTID_template import FC_GPT_ID
        return FC_GPT_ID(self)

    @property
    def FC_GATIN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGATIN_template import FC_GATIN
        return FC_GATIN(self)

    @property
    def FC_RFF_ID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCRFFID_template import FC_RFF_ID
        return FC_RFF_ID(self)

    @property
    def FC_RPNL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCRPNL_template import FC_RPNL
        return FC_RPNL(self)

    @property
    def FC_GDID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGDID_template import FC_GDID
        return FC_GDID(self)

    @property
    def FC_GTIN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGTIN_template import FC_GTIN
        return FC_GTIN(self)

    @property
    def FC_RPL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCRPL_template import FC_RPL
        return FC_RPL(self)

    @property
    def FC_GPLT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGPLT_template import FC_GPLT
        return FC_GPLT(self)

    @property
    def FC_RNN_ID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCRNNID_template import FC_RNN_ID
        return FC_RNN_ID(self)

    @property
    def FC_GPPN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGPPN_template import FC_GPPN
        return FC_GPPN(self)

    @property
    def FC_GPFCP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGPFCP_template import FC_GPFCP
        return FC_GPFCP(self)

    @property
    def FC_GPLI(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGPLI_template import FC_GPLI
        return FC_GPLI(self)

    @property
    def FC_GFN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGFN_template import FC_GFN
        return FC_GFN(self)

    @property
    def FC_DA_ID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCDAID_template import FC_DA_ID
        return FC_DA_ID(self)

    @property
    def FC_RPAB(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCRPAB_template import FC_RPAB
        return FC_RPAB(self)

    @property
    def FC_GFT_ID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGFTID_template import FC_GFT_ID
        return FC_GFT_ID(self)

    @property
    def FC_RSPN_ID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCRSPNID_template import FC_RSPN_ID
        return FC_RSPN_ID(self)

    @property
    def FC_GID_NN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGIDNN_template import FC_GID_NN
        return FC_GID_NN(self)

    @property
    def FC_GPN_ID(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCGPNID_template import FC_GPN_ID
        return FC_GPN_ID(self)

    @property
    def FC_EFP_SW_RJT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCEFPSWRJT_template import FC_EFP_SW_RJT
        return FC_EFP_SW_RJT(self)

    @property
    def FC_EFP_SW_ACC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCEFPSWACC_template import FC_EFP_SW_ACC
        return FC_EFP_SW_ACC(self)

    @property
    def FC_ESC_SW_ACC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCESCSWACC_template import FC_ESC_SW_ACC
        return FC_ESC_SW_ACC(self)

    @property
    def FC_RDI_SW_RJT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCRDISWRJT_template import FC_RDI_SW_RJT
        return FC_RDI_SW_RJT(self)

    @property
    def FC_MR_Request(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCMRRequest_template import FC_MR_Request
        return FC_MR_Request(self)

    @property
    def FC_LSA_Request(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCLSARequest_template import FC_LSA_Request
        return FC_LSA_Request(self)

    @property
    def FC_DIA_SW_RJT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCDIASWRJT_template import FC_DIA_SW_RJT
        return FC_DIA_SW_RJT(self)

    @property
    def FC_MR_SW_RJT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCMRSWRJT_template import FC_MR_SW_RJT
        return FC_MR_SW_RJT(self)

    @property
    def FC_DIA_SW_ACC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCDIASWACC_template import FC_DIA_SW_ACC
        return FC_DIA_SW_ACC(self)

    @property
    def FC_RDI_SW_ACC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCRDISWACC_template import FC_RDI_SW_ACC
        return FC_RDI_SW_ACC(self)

    @property
    def FC_ESC_SW_RJT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCESCSWRJT_template import FC_ESC_SW_RJT
        return FC_ESC_SW_RJT(self)

    @property
    def FC_LSU_Request(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCLSURequest_template import FC_LSU_Request
        return FC_LSU_Request(self)

    @property
    def FC_ESC_Request(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCESCRequest_template import FC_ESC_Request
        return FC_ESC_Request(self)

    @property
    def FC_ELP_SW_ACC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCELPSWACC_template import FC_ELP_SW_ACC
        return FC_ELP_SW_ACC(self)

    @property
    def FC_ELP_SW_RJT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCELPSWRJT_template import FC_ELP_SW_RJT
        return FC_ELP_SW_RJT(self)

    @property
    def FC_MR_SW_ACC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCMRSWACC_template import FC_MR_SW_ACC
        return FC_MR_SW_ACC(self)

    @property
    def FC_ELP_Request(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCELPRequest_template import FC_ELP_Request
        return FC_ELP_Request(self)

    @property
    def FC_DIA_Request(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCDIARequest_template import FC_DIA_Request
        return FC_DIA_Request(self)

    @property
    def FC_RDI_Request(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCRDIRequest_template import FC_RDI_Request
        return FC_RDI_Request(self)

    @property
    def FC_HLO_Request(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCHLORequest_template import FC_HLO_Request
        return FC_HLO_Request(self)

    @property
    def FC_EFP_Request(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.FCEFPRequest_template import FC_EFP_Request
        return FC_EFP_Request(self)

    @property
    def MAC_in_MAC_v42(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.macInMACv42_template import MAC_in_MAC_v42
        return MAC_in_MAC_v42(self)

    @property
    def PFC_PAUSE_8021Qbb(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pfcPause_template import PFC_PAUSE_8021Qbb
        return PFC_PAUSE_8021Qbb(self)

    @property
    def T_MPLS_Ethernet_Unicast(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.tmpls_template import T_MPLS_Ethernet_Unicast
        return T_MPLS_Ethernet_Unicast(self)

    @property
    def LLDP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lldp_template import LLDP
        return LLDP(self)

    @property
    def ECP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ecp_template import ECP
        return ECP(self)

    @property
    def ESMC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.esmc_template import ESMC
        return ESMC(self)

    @property
    def TRILL(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.trill_template import TRILL
        return TRILL(self)

    @property
    def TRILL_RB_Channel(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.trill_rb_channel_template import TRILL_RB_Channel
        return TRILL_RB_Channel(self)

    @property
    def TRILL_OAM_Echo_Request(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.trill_oam_echo_req_template import TRILL_OAM_Echo_Request
        return TRILL_OAM_Echo_Request(self)

    @property
    def TRILL_OAM_Echo_Reply(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.trill_oam_echo_reply_template import TRILL_OAM_Echo_Reply
        return TRILL_OAM_Echo_Reply(self)

    @property
    def FabricPath(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fabricpath_template import FabricPath
        return FabricPath(self)

    @property
    def PBB_Header(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pbb_template import PBB_Header
        return PBB_Header(self)

    @property
    def AVTP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.avtp_template import AVTP
        return AVTP(self)

    @property
    def MAC_Address_Acquisition_Header(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.maapHeader_template import MAC_Address_Acquisition_Header
        return MAC_Address_Acquisition_Header(self)

    @property
    def MSRP_Message(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.msrpMessage_template import MSRP_Message
        return MSRP_Message(self)

    @property
    def MSRP_Vector_Attribute(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.msrpVectorAttribute_template import MSRP_Vector_Attribute
        return MSRP_Vector_Attribute(self)

    @property
    def MMRP_Message(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mmrpMessage_template import MMRP_Message
        return MMRP_Message(self)

    @property
    def MMRP_Vector_Attribute(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mmrpVectorAttribute_template import MMRP_Vector_Attribute
        return MMRP_Vector_Attribute(self)

    @property
    def MVRP_Message(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mvrpMessage_template import MVRP_Message
        return MVRP_Message(self)

    @property
    def MVRP_Vector_Attribute(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mvrpVectorAttribute_template import MVRP_Vector_Attribute
        return MVRP_Vector_Attribute(self)

    @property
    def MRP_Three_Packed_Event(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mrpThreePackedEvent_template import MRP_Three_Packed_Event
        return MRP_Three_Packed_Event(self)

    @property
    def MRP_Four_Packed_Event(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mrpFourPackedEvent_template import MRP_Four_Packed_Event
        return MRP_Four_Packed_Event(self)

    @property
    def MRP_End_Mark(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.endMark_template import MRP_End_Mark
        return MRP_End_Mark(self)

    @property
    def BMAC_Header(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.bMacHeader_template import BMAC_Header
        return BMAC_Header(self)

    @property
    def BVLAN_Header(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.bVlanHeader_template import BVLAN_Header
        return BVLAN_Header(self)

    @property
    def I_Tag_Header(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.iTagHeader_template import I_Tag_Header
        return I_Tag_Header(self)

    @property
    def Preferred_PW_MPLS_Control_Word(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.preferredPwMplsCw_template import Preferred_PW_MPLS_Control_Word
        return Preferred_PW_MPLS_Control_Word(self)

    @property
    def R_Tag(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.r_Tag_template import R_Tag
        return R_Tag(self)

    @property
    def MACsec(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.macsec_template import MACsec
        return MACsec(self)

    @property
    def MACsec_HW(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.macsecHw_template import MACsec_HW
        return MACsec_HW(self)

    @property
    def Payload_Protocol_Type(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.payloadProtocolType_template import Payload_Protocol_Type
        return Payload_Protocol_Type(self)

    @property
    def AMT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.amt_template import AMT
        return AMT(self)

    @property
    def CGMP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.cgmp_template import CGMP
        return CGMP(self)

    @property
    def DDP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ddp_template import DDP
        return DDP(self)

    @property
    def IS_IS_Level_1_Complete_Sequence_Number_PDU(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisL1CSNPDU_template import IS_IS_Level_1_Complete_Sequence_Number_PDU
        return IS_IS_Level_1_Complete_Sequence_Number_PDU(self)

    @property
    def IS_IS_Level_1_LAN_Hello_PDU(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisLevel1LANHelloPDU_template import IS_IS_Level_1_LAN_Hello_PDU
        return IS_IS_Level_1_LAN_Hello_PDU(self)

    @property
    def IS_IS_Level_1_Link_State_PDU(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisLevel1LinkStatePDU_template import IS_IS_Level_1_Link_State_PDU
        return IS_IS_Level_1_Link_State_PDU(self)

    @property
    def IS_IS_Level_1_Partial_Sequence_Numbers_PDU(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisL1PSNPDU_template import IS_IS_Level_1_Partial_Sequence_Numbers_PDU
        return IS_IS_Level_1_Partial_Sequence_Numbers_PDU(self)

    @property
    def IS_IS_Level_2_Complete_Sequence_Number_PDU(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisL2CSNPDU_template import IS_IS_Level_2_Complete_Sequence_Number_PDU
        return IS_IS_Level_2_Complete_Sequence_Number_PDU(self)

    @property
    def IS_IS_Level_2_LAN_Hello_PDU(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisLevel2LANHelloPDU_template import IS_IS_Level_2_LAN_Hello_PDU
        return IS_IS_Level_2_LAN_Hello_PDU(self)

    @property
    def IS_IS_Level_2_Link_State_PDU(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisLevel2LinkStatePDU_template import IS_IS_Level_2_Link_State_PDU
        return IS_IS_Level_2_Link_State_PDU(self)

    @property
    def IS_IS_Level_2_Partial_Sequence_Numbers_PDU(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisL2PSNPDU_template import IS_IS_Level_2_Partial_Sequence_Numbers_PDU
        return IS_IS_Level_2_Partial_Sequence_Numbers_PDU(self)

    @property
    def IS_IS_Point_to_Point_Hello_PDU(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisPPPHelloPDU_template import IS_IS_Point_to_Point_Hello_PDU
        return IS_IS_Point_to_Point_Hello_PDU(self)

    @property
    def IS_IS_Level_1_MCAST_Complete_Sequence_Number_PDU(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisL1McastCSNPDU_template import IS_IS_Level_1_MCAST_Complete_Sequence_Number_PDU
        return IS_IS_Level_1_MCAST_Complete_Sequence_Number_PDU(self)

    @property
    def IS_IS_Level_1_MCAST_Link_State_PDU(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisL1McastLinkStatePDU_template import IS_IS_Level_1_MCAST_Link_State_PDU
        return IS_IS_Level_1_MCAST_Link_State_PDU(self)

    @property
    def IS_IS_Level_1_MCAST_Partial_Sequence_Numbers_PDU(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.isisL1McastPSNPDU_template import IS_IS_Level_1_MCAST_Partial_Sequence_Numbers_PDU
        return IS_IS_Level_1_MCAST_Partial_Sequence_Numbers_PDU(self)

    @property
    def IPv6_Authentication_Header(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6Authentication_template import IPv6_Authentication_Header
        return IPv6_Authentication_Header(self)

    @property
    def IPv6_Encapsulation_Header(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6Encapsulation_template import IPv6_Encapsulation_Header
        return IPv6_Encapsulation_Header(self)

    @property
    def IPv6_Pseudo_Header(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6Pseudo_template import IPv6_Pseudo_Header
        return IPv6_Pseudo_Header(self)

    @property
    def IPv6_Routing_Header(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6Routing_template import IPv6_Routing_Header
        return IPv6_Routing_Header(self)

    @property
    def IPv6_Routing_Header_Type_0(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6RoutingType0_template import IPv6_Routing_Header_Type_0
        return IPv6_Routing_Header_Type_0(self)

    @property
    def IPv6_Routing_Header_Type_2(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6RoutingType2_template import IPv6_Routing_Header_Type_2
        return IPv6_Routing_Header_Type_2(self)

    @property
    def IPv6_Routing_Header_Type_4(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6RoutingType4_template import IPv6_Routing_Header_Type_4
        return IPv6_Routing_Header_Type_4(self)

    @property
    def IPv4(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv4_template import IPv4
        return IPv4(self)

    @property
    def IPv6(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6_template import IPv6
        return IPv6(self)

    @property
    def IPv6_Fragment_Header(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6Fragment_template import IPv6_Fragment_Header
        return IPv6_Fragment_Header(self)

    @property
    def IPv6_Hop_by_Hop_Options_Header(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6HopByHopOptions_template import IPv6_Hop_by_Hop_Options_Header
        return IPv6_Hop_by_Hop_Options_Header(self)

    @property
    def IPv6_Hop_by_Hop_Options_With_IOAM_Header(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6HopByHopOptionsWithIOAM_template import IPv6_Hop_by_Hop_Options_With_IOAM_Header
        return IPv6_Hop_by_Hop_Options_With_IOAM_Header(self)

    @property
    def IPv6_Destination_Options_Header(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6DestinationOptions_template import IPv6_Destination_Options_Header
        return IPv6_Destination_Options_Header(self)

    @property
    def ICMP_Msg_Types__3_4_5_11_12(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.icmpv1_template import ICMP_Msg_Types__3_4_5_11_12
        return ICMP_Msg_Types__3_4_5_11_12(self)

    @property
    def ICMP_Msg_Types__0_8_13_14_15_16(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.icmpv2_template import ICMP_Msg_Types__0_8_13_14_15_16
        return ICMP_Msg_Types__0_8_13_14_15_16(self)

    @property
    def ICMP_Msg_Type__9(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.icmpv9_template import ICMP_Msg_Type__9
        return ICMP_Msg_Type__9(self)

    @property
    def ICMPv6(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.icmpv6_template import ICMPv6
        return ICMPv6(self)

    @property
    def IGMPv1(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.igmpv1_template import IGMPv1
        return IGMPv1(self)

    @property
    def IGMPv2(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.igmpv2_template import IGMPv2
        return IGMPv2(self)

    @property
    def IGMPv3_Membership_Query(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.igmpv3MembershipQuery_template import IGMPv3_Membership_Query
        return IGMPv3_Membership_Query(self)

    @property
    def IGMPv3_Membership_Report(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.igmpv3MembershipReport_template import IGMPv3_Membership_Report
        return IGMPv3_Membership_Report(self)

    @property
    def IPX(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipx_template import IPX
        return IPX(self)

    @property
    def GRE(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.gre_template import GRE
        return GRE(self)

    @property
    def GTPu_Optional_Fields(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.gTPuOptionalFields_template import GTPu_Optional_Fields
        return GTPu_Optional_Fields(self)

    @property
    def GTPu(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.gtpu_template import GTPu
        return GTPu(self)

    @property
    def L2TPv3_Control_Message_Over_IP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2TPv3ControlIP_template import L2TPv3_Control_Message_Over_IP
        return L2TPv3_Control_Message_Over_IP(self)

    @property
    def L2TPv3_Data_Message_Over_IP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2TPv3DataIP_template import L2TPv3_Data_Message_Over_IP
        return L2TPv3_Data_Message_Over_IP(self)

    @property
    def Minimal_IP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.minimalIP_template import Minimal_IP
        return Minimal_IP(self)

    @property
    def MLDv1(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mldv1_template import MLDv1
        return MLDv1(self)

    @property
    def MLDv2_Query(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mldv2Query_template import MLDv2_Query
        return MLDv2_Query(self)

    @property
    def MLDv2_Report(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mldv2Report_template import MLDv2_Report
        return MLDv2_Report(self)

    @property
    def Mobile_IPv6(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mobileIPv6_template import Mobile_IPv6
        return Mobile_IPv6(self)

    @property
    def NVGRE(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.nvgre_template import NVGRE
        return NVGRE(self)

    @property
    def OSPFv2_Hello_Packet(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv2Hello_template import OSPFv2_Hello_Packet
        return OSPFv2_Hello_Packet(self)

    @property
    def OSPFv2_Database_Description_Packet(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv2DatabaseDescription_template import OSPFv2_Database_Description_Packet
        return OSPFv2_Database_Description_Packet(self)

    @property
    def OSPFv2_LSA_ACK_Packet(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv2LSAAcknowledgement_template import OSPFv2_LSA_ACK_Packet
        return OSPFv2_LSA_ACK_Packet(self)

    @property
    def OSPFv2_LSA_Request_Packet(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv2LSARequest_template import OSPFv2_LSA_Request_Packet
        return OSPFv2_LSA_Request_Packet(self)

    @property
    def OSPFv2_LSA_Update_Packet(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv2LSAUpdate_template import OSPFv2_LSA_Update_Packet
        return OSPFv2_LSA_Update_Packet(self)

    @property
    def OSPFv3_Hello(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv3Hello_template import OSPFv3_Hello
        return OSPFv3_Hello(self)

    @property
    def OSPFv3_Database_Description_Packet(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv3DatabaseDescription_template import OSPFv3_Database_Description_Packet
        return OSPFv3_Database_Description_Packet(self)

    @property
    def OSPFv3_LSA_Acknowledgement_Packet(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv3LSAAcknowledgement_template import OSPFv3_LSA_Acknowledgement_Packet
        return OSPFv3_LSA_Acknowledgement_Packet(self)

    @property
    def OSPFv3_LSA_Request_Packet(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv3LSARequest_template import OSPFv3_LSA_Request_Packet
        return OSPFv3_LSA_Request_Packet(self)

    @property
    def OSPFv3_LSA_Update_Packet(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ospfv3LSAUpdate_template import OSPFv3_LSA_Update_Packet
        return OSPFv3_LSA_Update_Packet(self)

    @property
    def PIM_DM_Assert_Message(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimdmAssert_template import PIM_DM_Assert_Message
        return PIM_DM_Assert_Message(self)

    @property
    def PIM_DM_Graft_Graft_Ack_Message(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimdmGraftGraftAckMessage_template import PIM_DM_Graft_Graft_Ack_Message
        return PIM_DM_Graft_Graft_Ack_Message(self)

    @property
    def PIM_DM_Hello_Message(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimdmHelloMessage_template import PIM_DM_Hello_Message
        return PIM_DM_Hello_Message(self)

    @property
    def PIM_DM_Join_Prune_Message(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimdmJoinPruneMessage_template import PIM_DM_Join_Prune_Message
        return PIM_DM_Join_Prune_Message(self)

    @property
    def PIM_DM_State_Refresh_Message(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimdmStateRefresh_template import PIM_DM_State_Refresh_Message
        return PIM_DM_State_Refresh_Message(self)

    @property
    def PIM_Assert_Message(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimAssert_template import PIM_Assert_Message
        return PIM_Assert_Message(self)

    @property
    def PIM_Bootstrap_Message(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimBootstrapMessage_template import PIM_Bootstrap_Message
        return PIM_Bootstrap_Message(self)

    @property
    def PIM_Candidate_RP_Adv_Message(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimCandidateRPAdvMessage_template import PIM_Candidate_RP_Adv_Message
        return PIM_Candidate_RP_Adv_Message(self)

    @property
    def PIM_Hello_Message(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimHelloMessage_template import PIM_Hello_Message
        return PIM_Hello_Message(self)

    @property
    def PIM_Join_Prune_Message(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimJoinPruneMessage_template import PIM_Join_Prune_Message
        return PIM_Join_Prune_Message(self)

    @property
    def PIM_Register_Message(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimRegister_template import PIM_Register_Message
        return PIM_Register_Message(self)

    @property
    def PIM_Register_Stop_Message(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pimRegisterStopMessage_template import PIM_Register_Stop_Message
        return PIM_Register_Stop_Message(self)

    @property
    def RSVP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.rsvp_template import RSVP
        return RSVP(self)

    @property
    def RGMP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.rgmp_template import RGMP
        return RGMP(self)

    @property
    def RTMP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.rtmp_template import RTMP
        return RTMP(self)

    @property
    def VXLAN(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.vxlan_template import VXLAN
        return VXLAN(self)

    @property
    def Geneve(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.geneve_template import Geneve
        return Geneve(self)

    @property
    def Geneve_With_INT(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.genevewithtelemetry_template import Geneve_With_INT
        return Geneve_With_INT(self)

    @property
    def INT_Metadata(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.intmetadata_template import INT_Metadata
        return INT_Metadata(self)

    @property
    def INT_Shim_Header(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.intshimheader_template import INT_Shim_Header
        return INT_Shim_Header(self)

    @property
    def INT_Probe_Marker(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.intprobemarker_template import INT_Probe_Marker
        return INT_Probe_Marker(self)

    @property
    def BIER(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.bier_template import BIER
        return BIER(self)

    @property
    def eCPRI(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpri_template import eCPRI
        return eCPRI(self)

    @property
    def eCPRI_Msg_Type_IQ_Data0(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriMsgType0_template import eCPRI_Msg_Type_IQ_Data0
        return eCPRI_Msg_Type_IQ_Data0(self)

    @property
    def eCPRI_Msg_Type_Bit_Sequence1(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriMsgType1_template import eCPRI_Msg_Type_Bit_Sequence1
        return eCPRI_Msg_Type_Bit_Sequence1(self)

    @property
    def eCPRI_Msg_Type_Real_Time_Control_Data2(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriMsgType2_template import eCPRI_Msg_Type_Real_Time_Control_Data2
        return eCPRI_Msg_Type_Real_Time_Control_Data2(self)

    @property
    def eCPRI_Msg_Type_Generic_Data_Transfer3(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriMsgType3_template import eCPRI_Msg_Type_Generic_Data_Transfer3
        return eCPRI_Msg_Type_Generic_Data_Transfer3(self)

    @property
    def eCPRI_Msg_Type_Remote_Memory_Access4(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriMsgType4_template import eCPRI_Msg_Type_Remote_Memory_Access4
        return eCPRI_Msg_Type_Remote_Memory_Access4(self)

    @property
    def eCPRI_Msg_Type_One_way_Delay_Measurement5(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriMsgType5_template import eCPRI_Msg_Type_One_way_Delay_Measurement5
        return eCPRI_Msg_Type_One_way_Delay_Measurement5(self)

    @property
    def eCPRI_Msg_Type_Remote_Reset6(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriMsgType6_template import eCPRI_Msg_Type_Remote_Reset6
        return eCPRI_Msg_Type_Remote_Reset6(self)

    @property
    def eCPRI_Msg_Type_Event_Indication7(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriMsgType7_template import eCPRI_Msg_Type_Event_Indication7
        return eCPRI_Msg_Type_Event_Indication7(self)

    @property
    def eCPRI_Fault_Notify(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriFaultNotify_template import eCPRI_Fault_Notify
        return eCPRI_Fault_Notify(self)

    @property
    def eCPRI_User_Data(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.eCpriUserData_template import eCPRI_User_Data
        return eCPRI_User_Data(self)

    @property
    def TCP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.tcp_template import TCP
        return TCP(self)

    @property
    def UDP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.udp_template import UDP
        return UDP(self)

    @property
    def BFD_Bidirectional_Forwarding_Detection(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.bfd_template import BFD_Bidirectional_Forwarding_Detection
        return BFD_Bidirectional_Forwarding_Detection(self)

    @property
    def LISP_Map_Register(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lISPMapRegister_template import LISP_Map_Register
        return LISP_Map_Register(self)

    @property
    def LISP_Map_Request(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lISPMapRequest_template import LISP_Map_Request
        return LISP_Map_Request(self)

    @property
    def LISP_Map_Reply(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lISPMapReply_template import LISP_Map_Reply
        return LISP_Map_Reply(self)

    @property
    def LISP_Encapsulated_Control_Message(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lISPEncapsulatedControlMessage_template import LISP_Encapsulated_Control_Message
        return LISP_Encapsulated_Control_Message(self)

    @property
    def LISP_Map_Notify(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lISPMapNotify_template import LISP_Map_Notify
        return LISP_Map_Notify(self)

    @property
    def LISP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.lISP_template import LISP
        return LISP(self)

    @property
    def DHCP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.dhcp_template import DHCP
        return DHCP(self)

    @property
    def DNS_Query(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.dns_query_template import DNS_Query
        return DNS_Query(self)

    @property
    def DNS_Response(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.dns_response_template import DNS_Response
        return DNS_Response(self)

    @property
    def DHCP_With_Padding(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.dhcpWithPadding_template import DHCP_With_Padding
        return DHCP_With_Padding(self)

    @property
    def DHCPv6_Client_Server_Message(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.dhcpv6ClientServer_template import DHCPv6_Client_Server_Message
        return DHCPv6_Client_Server_Message(self)

    @property
    def DHCPv6_Relay_Agent_Server_Message(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.dhcpv6Relay_template import DHCPv6_Relay_Agent_Server_Message
        return DHCPv6_Relay_Agent_Server_Message(self)

    @property
    def LDP_Notification_Message(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpNotification_template import LDP_Notification_Message
        return LDP_Notification_Message(self)

    @property
    def LDP_Hello_Message(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpHello_template import LDP_Hello_Message
        return LDP_Hello_Message(self)

    @property
    def LDP_Initialization_Message(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpInitialization_template import LDP_Initialization_Message
        return LDP_Initialization_Message(self)

    @property
    def LDP_Keep_Alive_Message(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpKeepAlive_template import LDP_Keep_Alive_Message
        return LDP_Keep_Alive_Message(self)

    @property
    def LDP_Address_Message(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpAddress_template import LDP_Address_Message
        return LDP_Address_Message(self)

    @property
    def LDP_Address_Withdraw_Message(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpAddresWithdraw_template import LDP_Address_Withdraw_Message
        return LDP_Address_Withdraw_Message(self)

    @property
    def LDP_Label_Mapping_Message(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpLabelMapping_template import LDP_Label_Mapping_Message
        return LDP_Label_Mapping_Message(self)

    @property
    def LDP_Label_Request_Message(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpLabelRequest_template import LDP_Label_Request_Message
        return LDP_Label_Request_Message(self)

    @property
    def LDP_Label_Abort_Request_Message(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpLabelAbortRequest_template import LDP_Label_Abort_Request_Message
        return LDP_Label_Abort_Request_Message(self)

    @property
    def LDP_Label_Withdraw_Message(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpLabelWithdraw_template import LDP_Label_Withdraw_Message
        return LDP_Label_Withdraw_Message(self)

    @property
    def LDP_Label_Release_Message(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ldpLabelRelease_template import LDP_Label_Release_Message
        return LDP_Label_Release_Message(self)

    @property
    def L2TPv2_Control_Message(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2TPv2Control_template import L2TPv2_Control_Message
        return L2TPv2_Control_Message(self)

    @property
    def L2TPv2_Data_Message(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2TPv2Data_template import L2TPv2_Data_Message
        return L2TPv2_Data_Message(self)

    @property
    def L2TPv3_Control_Message_Over_UDP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2TPv3ControlUDP_template import L2TPv3_Control_Message_Over_UDP
        return L2TPv3_Control_Message_Over_UDP(self)

    @property
    def L2TPv3_Data_Message_Over_UDP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.l2TPv3DataUDP_template import L2TPv3_Data_Message_Over_UDP
        return L2TPv3_Data_Message_Over_UDP(self)

    @property
    def Mobile_IP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mobileIP_template import Mobile_IP
        return Mobile_IP(self)

    @property
    def MSDP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.msdp_template import MSDP
        return MSDP(self)

    @property
    def PTPv2___All_Messages(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.PTPv2_udp_template import PTPv2___All_Messages
        return PTPv2___All_Messages(self)

    @property
    def RIP1(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.rip1_template import RIP1
        return RIP1(self)

    @property
    def RIP2(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.rip2_template import RIP2
        return RIP2(self)

    @property
    def RIPng(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ripng_template import RIPng
        return RIPng(self)

    @property
    def RTP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.rtp_template import RTP
        return RTP(self)

    @property
    def HTTP_Get(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.HTTP_GET_template import HTTP_Get
        return HTTP_Get(self)

    @property
    def HTTP_200_OK(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.HTTP_200_OK_template import HTTP_200_OK
        return HTTP_200_OK(self)

    @property
    def RTSP_DESCRIBE(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.RTSP_DESCRIBE_template import RTSP_DESCRIBE
        return RTSP_DESCRIBE(self)

    @property
    def RTSP_Reply(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.RTSP_Reply_template import RTSP_Reply
        return RTSP_Reply(self)

    @property
    def IMAP_Request_Capability(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.IMAP_Request_Capability_template import IMAP_Request_Capability
        return IMAP_Request_Capability(self)

    @property
    def IMAP_Response_Capability_OK(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.IMAP_Response_Capability_OK_template import IMAP_Response_Capability_OK
        return IMAP_Response_Capability_OK(self)

    @property
    def POP_RETR_1(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.POP_RETR_1_template import POP_RETR_1
        return POP_RETR_1(self)

    @property
    def POP_OK(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.POP_OK_template import POP_OK
        return POP_OK(self)

    @property
    def SMTP_MAIL_FROM(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.SMTP_MAIL_FROM_template import SMTP_MAIL_FROM
        return SMTP_MAIL_FROM(self)

    @property
    def SMTP_250_OK(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.SMTP_250_OK_template import SMTP_250_OK
        return SMTP_250_OK(self)

    @property
    def TDS_Remote_Procedure_Call(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.TDS_Remote_Procedure_Call_template import TDS_Remote_Procedure_Call
        return TDS_Remote_Procedure_Call(self)

    @property
    def TDS_Response(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.TDS_Response_template import TDS_Response
        return TDS_Response(self)

    @property
    def iSCSI_Data_Out(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.iSCSI_Data_Out_template import iSCSI_Data_Out
        return iSCSI_Data_Out(self)

    @property
    def iSCSI_Data_In(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.iSCSI_Data_In_template import iSCSI_Data_In
        return iSCSI_Data_In(self)

    @property
    def NTP(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ntp_template import NTP
        return NTP(self)

    @property
    def Custom(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.custom_template import Custom
        return Custom(self)

    @property
    def FC(self):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.fc_template import FC
        return FC(self)

    @property
    def DisplayName(self):
        """
        Returns
        -------
        - str: The display name of the stack.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DisplayName'])

    @property
    def StackTypeId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['StackTypeId'])

    @property
    def TemplateName(self):
        """
        Returns
        -------
        - str: Indiates the protocol template name that is added to a packet in a stack.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TemplateName'])

    def find(self, DisplayName=None, StackTypeId=None, TemplateName=None):
        """Finds and retrieves stack resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve stack resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all stack resources from the server.

        Args
        ----
        - DisplayName (str): The display name of the stack.
        - StackTypeId (str): 
        - TemplateName (str): Indiates the protocol template name that is added to a packet in a stack.

        Returns
        -------
        - self: This instance with matching stack resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of stack data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the stack resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Append(self, *args, **kwargs):
        """Executes the append operation on the server.

        Append a protocol template after the specified stack object reference.

        DEPRECATED append(Arg2=href)string
        ----------------------------------
        - Arg2 (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../protocolTemplate)): A valid /traffic/protocolTemplate object reference.
        - Returns str: This exec returns an object reference to the newly appended stack item.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('append', payload=payload, response_object=None)

    def AppendProtocol(self, *args, **kwargs):
        """Executes the appendProtocol operation on the server.

        Append a protocol template after the specified stack object reference.

        appendProtocol(Arg2=href)href
        -----------------------------
        - Arg2 (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../protocolTemplate)): A valid /traffic/protocolTemplate object reference.
        - Returns str(None | /api/v1/sessions/1/ixnetwork/traffic/.../stack): This exec returns an object reference to the newly appended stack item.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('appendProtocol', payload=payload, response_object=None)

    def GetValidProtocols(self):
        """Executes the getValidProtocols operation on the server.

        Retrieves the list of recommended protocols that can be added on top of the current protocol.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('getValidProtocols', payload=payload, response_object=None)

    def Insert(self, *args, **kwargs):
        """Executes the insert operation on the server.

        Insert a protocol template before the specified stack object reference.

        DEPRECATED insert(Arg2=href)string
        ----------------------------------
        - Arg2 (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../protocolTemplate)): A valid /traffic/protocolTemplate object reference
        - Returns str: This exec returns an object reference to the newly inserted stack item.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('insert', payload=payload, response_object=None)

    def InsertProtocol(self, *args, **kwargs):
        """Executes the insertProtocol operation on the server.

        Insert a protocol template before the specified stack object reference.

        insertProtocol(Arg2=href)href
        -----------------------------
        - Arg2 (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../protocolTemplate)): A valid /traffic/protocolTemplate object reference
        - Returns str(None | /api/v1/sessions/1/ixnetwork/traffic/.../stack): This exec returns an object reference to the newly inserted stack item.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('insertProtocol', payload=payload, response_object=None)

    def Remove(self):
        """Executes the remove operation on the server.

        Delete the specified stack object reference.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('remove', payload=payload, response_object=None)
