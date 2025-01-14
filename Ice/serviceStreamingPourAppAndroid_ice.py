# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.10
#
# <auto-generated>
#
# Generated from file `serviceStreamingPourAppAndroid.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module StreamingAndroid
_M_StreamingAndroid = Ice.openModule('StreamingAndroid')
__name__ = 'StreamingAndroid'

if 'Song' not in _M_StreamingAndroid.__dict__:
    _M_StreamingAndroid.Song = Ice.createTempClass()
    class Song(object):
        def __init__(self, title='', artist='', type='', dateofrelease='', emplacement=''):
            self.title = title
            self.artist = artist
            self.type = type
            self.dateofrelease = dateofrelease
            self.emplacement = emplacement

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.title)
            _h = 5 * _h + Ice.getHash(self.artist)
            _h = 5 * _h + Ice.getHash(self.type)
            _h = 5 * _h + Ice.getHash(self.dateofrelease)
            _h = 5 * _h + Ice.getHash(self.emplacement)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_StreamingAndroid.Song):
                return NotImplemented
            else:
                if self.title is None or other.title is None:
                    if self.title != other.title:
                        return (-1 if self.title is None else 1)
                else:
                    if self.title < other.title:
                        return -1
                    elif self.title > other.title:
                        return 1
                if self.artist is None or other.artist is None:
                    if self.artist != other.artist:
                        return (-1 if self.artist is None else 1)
                else:
                    if self.artist < other.artist:
                        return -1
                    elif self.artist > other.artist:
                        return 1
                if self.type is None or other.type is None:
                    if self.type != other.type:
                        return (-1 if self.type is None else 1)
                else:
                    if self.type < other.type:
                        return -1
                    elif self.type > other.type:
                        return 1
                if self.dateofrelease is None or other.dateofrelease is None:
                    if self.dateofrelease != other.dateofrelease:
                        return (-1 if self.dateofrelease is None else 1)
                else:
                    if self.dateofrelease < other.dateofrelease:
                        return -1
                    elif self.dateofrelease > other.dateofrelease:
                        return 1
                if self.emplacement is None or other.emplacement is None:
                    if self.emplacement != other.emplacement:
                        return (-1 if self.emplacement is None else 1)
                else:
                    if self.emplacement < other.emplacement:
                        return -1
                    elif self.emplacement > other.emplacement:
                        return 1
                return 0

        def __lt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r < 0

        def __le__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r <= 0

        def __gt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r > 0

        def __ge__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r >= 0

        def __eq__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r == 0

        def __ne__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r != 0

        def __str__(self):
            return IcePy.stringify(self, _M_StreamingAndroid._t_Song)

        __repr__ = __str__

    _M_StreamingAndroid._t_Song = IcePy.defineStruct('::StreamingAndroid::Song', Song, (), (
        ('title', (), IcePy._t_string),
        ('artist', (), IcePy._t_string),
        ('type', (), IcePy._t_string),
        ('dateofrelease', (), IcePy._t_string),
        ('emplacement', (), IcePy._t_string)
    ))

    _M_StreamingAndroid.Song = Song
    del Song

if 'SongNotFoundException' not in _M_StreamingAndroid.__dict__:
    _M_StreamingAndroid.SongNotFoundException = Ice.createTempClass()
    class SongNotFoundException(Ice.UserException):
        def __init__(self, reason=''):
            self.reason = reason

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::StreamingAndroid::SongNotFoundException'

    _M_StreamingAndroid._t_SongNotFoundException = IcePy.defineException('::StreamingAndroid::SongNotFoundException', SongNotFoundException, (), False, None, (('reason', (), IcePy._t_string, False, 0),))
    SongNotFoundException._ice_type = _M_StreamingAndroid._t_SongNotFoundException

    _M_StreamingAndroid.SongNotFoundException = SongNotFoundException
    del SongNotFoundException

_M_StreamingAndroid._t_InterfaceStreamingAndroid = IcePy.defineValue('::StreamingAndroid::InterfaceStreamingAndroid', Ice.Value, -1, (), False, True, None, ())

if 'InterfaceStreamingAndroidPrx' not in _M_StreamingAndroid.__dict__:
    _M_StreamingAndroid.InterfaceStreamingAndroidPrx = Ice.createTempClass()
    class InterfaceStreamingAndroidPrx(Ice.ObjectPrx):

        def streamAudioWithTitle(self, titreExtraitAvecNlp, context=None):
            return _M_StreamingAndroid.InterfaceStreamingAndroid._op_streamAudioWithTitle.invoke(self, ((titreExtraitAvecNlp, ), context))

        def streamAudioWithTitleAsync(self, titreExtraitAvecNlp, context=None):
            return _M_StreamingAndroid.InterfaceStreamingAndroid._op_streamAudioWithTitle.invokeAsync(self, ((titreExtraitAvecNlp, ), context))

        def begin_streamAudioWithTitle(self, titreExtraitAvecNlp, _response=None, _ex=None, _sent=None, context=None):
            return _M_StreamingAndroid.InterfaceStreamingAndroid._op_streamAudioWithTitle.begin(self, ((titreExtraitAvecNlp, ), _response, _ex, _sent, context))

        def end_streamAudioWithTitle(self, _r):
            return _M_StreamingAndroid.InterfaceStreamingAndroid._op_streamAudioWithTitle.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_StreamingAndroid.InterfaceStreamingAndroidPrx.ice_checkedCast(proxy, '::StreamingAndroid::InterfaceStreamingAndroid', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_StreamingAndroid.InterfaceStreamingAndroidPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::StreamingAndroid::InterfaceStreamingAndroid'
    _M_StreamingAndroid._t_InterfaceStreamingAndroidPrx = IcePy.defineProxy('::StreamingAndroid::InterfaceStreamingAndroid', InterfaceStreamingAndroidPrx)

    _M_StreamingAndroid.InterfaceStreamingAndroidPrx = InterfaceStreamingAndroidPrx
    del InterfaceStreamingAndroidPrx

    _M_StreamingAndroid.InterfaceStreamingAndroid = Ice.createTempClass()
    class InterfaceStreamingAndroid(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::StreamingAndroid::InterfaceStreamingAndroid')

        def ice_id(self, current=None):
            return '::StreamingAndroid::InterfaceStreamingAndroid'

        @staticmethod
        def ice_staticId():
            return '::StreamingAndroid::InterfaceStreamingAndroid'

        def streamAudioWithTitle(self, titreExtraitAvecNlp, current=None):
            raise NotImplementedError("servant method 'streamAudioWithTitle' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_StreamingAndroid._t_InterfaceStreamingAndroidDisp)

        __repr__ = __str__

    _M_StreamingAndroid._t_InterfaceStreamingAndroidDisp = IcePy.defineClass('::StreamingAndroid::InterfaceStreamingAndroid', InterfaceStreamingAndroid, (), None, ())
    InterfaceStreamingAndroid._ice_type = _M_StreamingAndroid._t_InterfaceStreamingAndroidDisp

    InterfaceStreamingAndroid._op_streamAudioWithTitle = IcePy.Operation('streamAudioWithTitle', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), IcePy._t_string, False, 0), (_M_StreamingAndroid._t_SongNotFoundException,))

    _M_StreamingAndroid.InterfaceStreamingAndroid = InterfaceStreamingAndroid
    del InterfaceStreamingAndroid

# End of module StreamingAndroid
