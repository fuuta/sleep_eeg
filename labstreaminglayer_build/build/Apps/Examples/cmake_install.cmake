# Install script for directory: /Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/Apps/Examples

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/Examples" TYPE EXECUTABLE FILES "/Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/build/Apps/Examples/CppSendRand")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/Examples/CppSendRand" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/Examples/CppSendRand")
    execute_process(COMMAND /usr/bin/install_name_tool
      -delete_rpath "/Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/build/LSL/liblsl"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/Examples/CppSendRand")
    execute_process(COMMAND /usr/bin/install_name_tool
      -add_rpath "@executable_path/../LSL/lib"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/Examples/CppSendRand")
    execute_process(COMMAND /usr/bin/install_name_tool
      -add_rpath "@executable_path/"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/Examples/CppSendRand")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/Examples/CppSendRand")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/Examples" TYPE FILE FILES "/Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/build/LSL/liblsl/liblsl64.1.4.0.dylib")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/Examples" TYPE EXECUTABLE FILES "/Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/build/Apps/Examples/CppReceive")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/Examples/CppReceive" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/Examples/CppReceive")
    execute_process(COMMAND /usr/bin/install_name_tool
      -delete_rpath "/Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/build/LSL/liblsl"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/Examples/CppReceive")
    execute_process(COMMAND /usr/bin/install_name_tool
      -add_rpath "@executable_path/../LSL/lib"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/Examples/CppReceive")
    execute_process(COMMAND /usr/bin/install_name_tool
      -add_rpath "@executable_path/"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/Examples/CppReceive")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/Examples/CppReceive")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/Examples" TYPE FILE FILES "/Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/build/LSL/liblsl/liblsl64.1.4.0.dylib")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/Examples" TYPE EXECUTABLE FILES "/Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/build/Apps/Examples/SendDataC")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/Examples/SendDataC" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/Examples/SendDataC")
    execute_process(COMMAND /usr/bin/install_name_tool
      -delete_rpath "/Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/build/LSL/liblsl"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/Examples/SendDataC")
    execute_process(COMMAND /usr/bin/install_name_tool
      -add_rpath "@executable_path/../LSL/lib"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/Examples/SendDataC")
    execute_process(COMMAND /usr/bin/install_name_tool
      -add_rpath "@executable_path/"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/Examples/SendDataC")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/Examples/SendDataC")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/Examples" TYPE FILE FILES "/Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/build/LSL/liblsl/liblsl64.1.4.0.dylib")
endif()

