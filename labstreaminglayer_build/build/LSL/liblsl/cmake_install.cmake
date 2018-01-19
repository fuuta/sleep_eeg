# Install script for directory: /Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/LSL/liblsl

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/build/install/lsl_Release")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/LSL/lib" TYPE SHARED_LIBRARY FILES
    "/Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/build/LSL/liblsl/liblsl64.1.4.0.dylib"
    "/Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/build/LSL/liblsl/liblsl64.dylib"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/LSL/lib/liblsl64.1.4.0.dylib"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/LSL/lib/liblsl64.dylib"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      if(CMAKE_INSTALL_DO_STRIP)
        execute_process(COMMAND "/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/strip" "${file}")
      endif()
    endif()
  endforeach()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/LSL/cmake/LSLConfig.cmake")
    file(DIFFERENT EXPORT_FILE_CHANGED FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/LSL/cmake/LSLConfig.cmake"
         "/Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/build/LSL/liblsl/CMakeFiles/Export/LSL/cmake/LSLConfig.cmake")
    if(EXPORT_FILE_CHANGED)
      file(GLOB OLD_CONFIG_FILES "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/LSL/cmake/LSLConfig-*.cmake")
      if(OLD_CONFIG_FILES)
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/LSL/cmake/LSLConfig.cmake\" will be replaced.  Removing files [${OLD_CONFIG_FILES}].")
        file(REMOVE ${OLD_CONFIG_FILES})
      endif()
    endif()
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/LSL/cmake" TYPE FILE FILES "/Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/build/LSL/liblsl/CMakeFiles/Export/LSL/cmake/LSLConfig.cmake")
  if("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/LSL/cmake" TYPE FILE FILES "/Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/build/LSL/liblsl/CMakeFiles/Export/LSL/cmake/LSLConfig-release.cmake")
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/LSL/include" TYPE FILE FILES
    "/Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/LSL/liblsl/include/lsl_c.h"
    "/Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/LSL/liblsl/include/lsl_cpp.h"
    )
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/build/LSL/liblsl/external/cmake_install.cmake")

endif()

