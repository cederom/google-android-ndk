LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)
LOCAL_MODULE := foo
LOCAL_SRC_FILES := foo.cpp
LOCAL_BRANCH_PROTECTION := standard
include $(BUILD_SHARED_LIBRARY)
