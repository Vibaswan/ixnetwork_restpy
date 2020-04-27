# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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


class GeneralLearnedInfo(Base):
    """This object holds lists of the general learned route information.
    The GeneralLearnedInfo class encapsulates a list of generalLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the GeneralLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'generalLearnedInfo'

    def __init__(self, parent):
        super(GeneralLearnedInfo, self).__init__(parent)

    @property
    def AverageRtt(self):
        """
        Returns
        -------
        - str: This signifies the average Round Trip Time.
        """
        return self._get_attribute('averageRtt')

    @property
    def BfdSessionMyState(self):
        """
        Returns
        -------
        - str: This signifies the window provides read-only information about the state of BFD interface on the specified emulated router.
        """
        return self._get_attribute('bfdSessionMyState')

    @property
    def BfdSessionPeerState(self):
        """
        Returns
        -------
        - str: This signifies the state of the far side of the BFD session, either active or not.
        """
        return self._get_attribute('bfdSessionPeerState')

    @property
    def CcInUse(self):
        """
        Returns
        -------
        - str: This signifies the Continuity Check in use. The values are RA, PW-ACH, or TTL Exp.
        """
        return self._get_attribute('ccInUse')

    @property
    def CvInUse(self):
        """
        Returns
        -------
        - str: This signifies the Connectivity Verification in use. The values are LSP Ping, BFD IP/UDP, or LSP Ping.
        """
        return self._get_attribute('cvInUse')

    @property
    def Fec(self):
        """
        Returns
        -------
        - str: This signifies the FEC component.
        """
        return self._get_attribute('fec')

    @property
    def IncomingLabelStack(self):
        """
        Returns
        -------
        - str: This signifies the BGP sends the assigned labels information to this MPLS OAM module which is used for validation of FEC stack received in an echo request.
        """
        return self._get_attribute('incomingLabelStack')

    @property
    def IncomingLspLabel(self):
        """
        Returns
        -------
        - str: This signifies the incoming LSP label value.
        """
        return self._get_attribute('incomingLspLabel')

    @property
    def IncomingPwLabel(self):
        """
        Returns
        -------
        - str: This signifies the incoming PW label value.
        """
        return self._get_attribute('incomingPwLabel')

    @property
    def LspPingReachability(self):
        """
        Returns
        -------
        - str: This signifies the specification of whether the queried LSP Ping could be reached or not.
        """
        return self._get_attribute('lspPingReachability')

    @property
    def MaxRtt(self):
        """
        Returns
        -------
        - str: This signifies the specification of the maximum Round Trip Time.
        """
        return self._get_attribute('maxRtt')

    @property
    def MinRtt(self):
        """
        Returns
        -------
        - str: This signifies the specification of the minimum Round Trip Time.
        """
        return self._get_attribute('minRtt')

    @property
    def MyDiscriminator(self):
        """
        Returns
        -------
        - number: This signifies the discriminator for the session on this interface.
        """
        return self._get_attribute('myDiscriminator')

    @property
    def MyIpAddress(self):
        """
        Returns
        -------
        - str: This signifies the IP address for this interface.
        """
        return self._get_attribute('myIpAddress')

    @property
    def OutgoingLabelStack(self):
        """
        Returns
        -------
        - str: This signifies the BGP sends the assigned labels information to this MPLS OAM module which is used for validation of FEC outgoing Label stack that is received in an echo request.
        """
        return self._get_attribute('outgoingLabelStack')

    @property
    def OutgoingLspLabel(self):
        """
        Returns
        -------
        - str: This signifies the outgoing LSP label value.
        """
        return self._get_attribute('outgoingLspLabel')

    @property
    def OutgoingPwLabel(self):
        """
        Returns
        -------
        - str: This signifies the outgoing PW label value.
        """
        return self._get_attribute('outgoingPwLabel')

    @property
    def PeerDiscriminator(self):
        """
        Returns
        -------
        - number: This signifies the discriminator for the far side of the session.
        """
        return self._get_attribute('peerDiscriminator')

    @property
    def PeerIpAddress(self):
        """
        Returns
        -------
        - str: This signifies the learnt IP address for the session.
        """
        return self._get_attribute('peerIpAddress')

    @property
    def PingAttempts(self):
        """
        Returns
        -------
        - number: This signifies the specification of the number of ping attempts.
        """
        return self._get_attribute('pingAttempts')

    @property
    def PingFailures(self):
        """
        Returns
        -------
        - number: This signifies the specification of the number of ping failures.
        """
        return self._get_attribute('pingFailures')

    @property
    def PingReplyTx(self):
        """
        Returns
        -------
        - number: This signifies the specification of the number of ping reply transmitted at regular intervals.
        """
        return self._get_attribute('pingReplyTx')

    @property
    def PingRequestRx(self):
        """
        Returns
        -------
        - number: This signifies the specification of the number of ping request received at regular intervals.
        """
        return self._get_attribute('pingRequestRx')

    @property
    def PingSuccess(self):
        """
        Returns
        -------
        - number: This signifies the specification of the rate of ping success.
        """
        return self._get_attribute('pingSuccess')

    @property
    def ReceivedMinRxInterval(self):
        """
        Returns
        -------
        - number: This signifies the minimum receive interval, in milliseconds, for the far side of the session.
        """
        return self._get_attribute('receivedMinRxInterval')

    @property
    def ReceivedMultiplier(self):
        """
        Returns
        -------
        - number: This signifies the number of received negotiated transmit intervals when multiplied by this value, provides the detection time for the interface.
        """
        return self._get_attribute('receivedMultiplier')

    @property
    def ReceivedPeerFlags(self):
        """
        Returns
        -------
        - str: This signifies the number of peer generated flags received.
        """
        return self._get_attribute('receivedPeerFlags')

    @property
    def ReceivedTxInterval(self):
        """
        Returns
        -------
        - number: This signifies the minimum transmit interval, in milliseconds, for the far side of the session.
        """
        return self._get_attribute('receivedTxInterval')

    @property
    def ReturnCode(self):
        """
        Returns
        -------
        - str: This signifies the return code value.
        """
        return self._get_attribute('returnCode')

    @property
    def ReturnSubcode(self):
        """
        Returns
        -------
        - number: This signifies the return subcode value.
        """
        return self._get_attribute('returnSubcode')

    @property
    def SignalingProtocol(self):
        """
        Returns
        -------
        - str: This signifies the options for signaling protocol are BGP, LDP, RSVP.
        """
        return self._get_attribute('signalingProtocol')

    @property
    def TunnelEndpointType(self):
        """
        Returns
        -------
        - str: This signifies the tunnel endpoint type options include Ingress, Egress, Bi-directional.
        """
        return self._get_attribute('tunnelEndpointType')

    @property
    def TunnelType(self):
        """
        Returns
        -------
        - str: This signifies the tunnel type options include LSP and PW.
        """
        return self._get_attribute('tunnelType')

    def find(self, AverageRtt=None, BfdSessionMyState=None, BfdSessionPeerState=None, CcInUse=None, CvInUse=None, Fec=None, IncomingLabelStack=None, IncomingLspLabel=None, IncomingPwLabel=None, LspPingReachability=None, MaxRtt=None, MinRtt=None, MyDiscriminator=None, MyIpAddress=None, OutgoingLabelStack=None, OutgoingLspLabel=None, OutgoingPwLabel=None, PeerDiscriminator=None, PeerIpAddress=None, PingAttempts=None, PingFailures=None, PingReplyTx=None, PingRequestRx=None, PingSuccess=None, ReceivedMinRxInterval=None, ReceivedMultiplier=None, ReceivedPeerFlags=None, ReceivedTxInterval=None, ReturnCode=None, ReturnSubcode=None, SignalingProtocol=None, TunnelEndpointType=None, TunnelType=None):
        """Finds and retrieves generalLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve generalLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all generalLearnedInfo resources from the server.

        Args
        ----
        - AverageRtt (str): This signifies the average Round Trip Time.
        - BfdSessionMyState (str): This signifies the window provides read-only information about the state of BFD interface on the specified emulated router.
        - BfdSessionPeerState (str): This signifies the state of the far side of the BFD session, either active or not.
        - CcInUse (str): This signifies the Continuity Check in use. The values are RA, PW-ACH, or TTL Exp.
        - CvInUse (str): This signifies the Connectivity Verification in use. The values are LSP Ping, BFD IP/UDP, or LSP Ping.
        - Fec (str): This signifies the FEC component.
        - IncomingLabelStack (str): This signifies the BGP sends the assigned labels information to this MPLS OAM module which is used for validation of FEC stack received in an echo request.
        - IncomingLspLabel (str): This signifies the incoming LSP label value.
        - IncomingPwLabel (str): This signifies the incoming PW label value.
        - LspPingReachability (str): This signifies the specification of whether the queried LSP Ping could be reached or not.
        - MaxRtt (str): This signifies the specification of the maximum Round Trip Time.
        - MinRtt (str): This signifies the specification of the minimum Round Trip Time.
        - MyDiscriminator (number): This signifies the discriminator for the session on this interface.
        - MyIpAddress (str): This signifies the IP address for this interface.
        - OutgoingLabelStack (str): This signifies the BGP sends the assigned labels information to this MPLS OAM module which is used for validation of FEC outgoing Label stack that is received in an echo request.
        - OutgoingLspLabel (str): This signifies the outgoing LSP label value.
        - OutgoingPwLabel (str): This signifies the outgoing PW label value.
        - PeerDiscriminator (number): This signifies the discriminator for the far side of the session.
        - PeerIpAddress (str): This signifies the learnt IP address for the session.
        - PingAttempts (number): This signifies the specification of the number of ping attempts.
        - PingFailures (number): This signifies the specification of the number of ping failures.
        - PingReplyTx (number): This signifies the specification of the number of ping reply transmitted at regular intervals.
        - PingRequestRx (number): This signifies the specification of the number of ping request received at regular intervals.
        - PingSuccess (number): This signifies the specification of the rate of ping success.
        - ReceivedMinRxInterval (number): This signifies the minimum receive interval, in milliseconds, for the far side of the session.
        - ReceivedMultiplier (number): This signifies the number of received negotiated transmit intervals when multiplied by this value, provides the detection time for the interface.
        - ReceivedPeerFlags (str): This signifies the number of peer generated flags received.
        - ReceivedTxInterval (number): This signifies the minimum transmit interval, in milliseconds, for the far side of the session.
        - ReturnCode (str): This signifies the return code value.
        - ReturnSubcode (number): This signifies the return subcode value.
        - SignalingProtocol (str): This signifies the options for signaling protocol are BGP, LDP, RSVP.
        - TunnelEndpointType (str): This signifies the tunnel endpoint type options include Ingress, Egress, Bi-directional.
        - TunnelType (str): This signifies the tunnel type options include LSP and PW.

        Returns
        -------
        - self: This instance with matching generalLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of generalLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the generalLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def AddRecordForTrigger(self):
        """Executes the addRecordForTrigger operation on the server.

        This signifies the record added for trigger settings.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('addRecordForTrigger', payload=payload, response_object=None)
