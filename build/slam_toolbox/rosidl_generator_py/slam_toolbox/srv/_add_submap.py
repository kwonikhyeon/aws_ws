# generated from rosidl_generator_py/resource/_idl.py.em
# with input from slam_toolbox:srv/AddSubmap.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_AddSubmap_Request(type):
    """Metaclass of message 'AddSubmap_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('slam_toolbox')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'slam_toolbox.srv.AddSubmap_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__add_submap__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__add_submap__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__add_submap__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__add_submap__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__add_submap__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AddSubmap_Request(metaclass=Metaclass_AddSubmap_Request):
    """Message class 'AddSubmap_Request'."""

    __slots__ = [
        '_filename',
    ]

    _fields_and_field_types = {
        'filename': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.filename = kwargs.get('filename', str())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.filename != other.filename:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def filename(self):
        """Message field 'filename'."""
        return self._filename

    @filename.setter
    def filename(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'filename' field must be of type 'str'"
        self._filename = value


# Import statements for member types

# already imported above
# import rosidl_parser.definition


class Metaclass_AddSubmap_Response(type):
    """Metaclass of message 'AddSubmap_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('slam_toolbox')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'slam_toolbox.srv.AddSubmap_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__add_submap__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__add_submap__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__add_submap__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__add_submap__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__add_submap__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AddSubmap_Response(metaclass=Metaclass_AddSubmap_Response):
    """Message class 'AddSubmap_Response'."""

    __slots__ = [
    ]

    _fields_and_field_types = {
    }

    SLOT_TYPES = (
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)


class Metaclass_AddSubmap(type):
    """Metaclass of service 'AddSubmap'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('slam_toolbox')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'slam_toolbox.srv.AddSubmap')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__add_submap

            from slam_toolbox.srv import _add_submap
            if _add_submap.Metaclass_AddSubmap_Request._TYPE_SUPPORT is None:
                _add_submap.Metaclass_AddSubmap_Request.__import_type_support__()
            if _add_submap.Metaclass_AddSubmap_Response._TYPE_SUPPORT is None:
                _add_submap.Metaclass_AddSubmap_Response.__import_type_support__()


class AddSubmap(metaclass=Metaclass_AddSubmap):
    from slam_toolbox.srv._add_submap import AddSubmap_Request as Request
    from slam_toolbox.srv._add_submap import AddSubmap_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
