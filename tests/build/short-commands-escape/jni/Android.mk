LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)
LOCAL_MODULE := libfoo
LOCAL_SRC_FILES := foo.cpp
LOCAL_SHORT_COMMANDS := true
include $(BUILD_STATIC_LIBRARY)

include $(CLEAR_VARS)
LOCAL_MODULE := libbar
LOCAL_SRC_FILES := bar.cpp
LOCAL_SHORT_COMMANDS := true
LOCAL_STATIC_LIBRARIES := libfoo
include $(BUILD_SHARED_LIBRARY)