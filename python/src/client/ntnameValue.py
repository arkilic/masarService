# ntnameValue.py
#
# Copyright - See the COPYRIGHT that is included with this distribution.
# EPICS pvService is distributed subject to a Software License Agreement
#    found in file LICENSE that is included with this distribution.
# Author Marty Kraimer 2011.07

import ntnameValuePy

class NTNameValue(object) :
    """Create a NTNameValue

    """
    def __init__(self,function,dictionary) :
        """Constructor
         Creates a C++ NTNameValue and a python wrapper for the NTNameValue.

        function A string that specifies a function name.
        dictionary A python dictionary that is a sequence of name,value pairs"""
        self.cppPvt = ntnameValuePy._init(self,function,dictionary)
    def __del__(self) :
        """Destructor Destroy the C++ NTNameValue"""
        ntnameValuePy._destroy(self.cppPvt)
    def __str__(self) :
        """Get a string value for the NTNameValue."""
        return ntnameValuePy.__str__(self.cppPvt)
    def getNTNameValue(self) :
        """Get a python object that can be passed to
        another python method that is a wrapper to a C++ method
        that expects a PVStructure object."""
        return ntnameValuePy._getNTNameValuePy(self.cppPvt);