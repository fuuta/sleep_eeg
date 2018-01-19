# Install script for directory: /Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/Apps/XDFBrowser

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/XDFBrowser" TYPE DIRECTORY FILES "/Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/build/Apps/XDFBrowser/XDFBrowser.app" USE_SOURCE_PERMISSIONS)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/XDFBrowser/XDFBrowser.app/Contents/MacOS/XDFBrowser" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/XDFBrowser/XDFBrowser.app/Contents/MacOS/XDFBrowser")
    execute_process(COMMAND /usr/bin/install_name_tool
      -delete_rpath "/Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/build/LSL/liblsl"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/XDFBrowser/XDFBrowser.app/Contents/MacOS/XDFBrowser")
    execute_process(COMMAND /usr/bin/install_name_tool
      -add_rpath "@executable_path/../LSL/lib"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/XDFBrowser/XDFBrowser.app/Contents/MacOS/XDFBrowser")
    execute_process(COMMAND /usr/bin/install_name_tool
      -add_rpath "@executable_path/"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/XDFBrowser/XDFBrowser.app/Contents/MacOS/XDFBrowser")
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/XDFBrowser/XDFBrowser.app/Contents/MacOS" TYPE FILE FILES "/Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/build/LSL/liblsl/liblsl64.1.4.0.dylib")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  
					message(STATUS "Running Qt Deploy Tool...")
					#list(APPEND QT_DEPLOYQT_FLAGS -dmg)
					if(CMAKE_INSTALL_CONFIG_NAME STREQUAL "Debug")
					    list(APPEND QT_DEPLOYQT_FLAGS -use-debug-libs)
					endif()
					execute_process(COMMAND
						"/usr/local/Cellar/qt/5.10.0/bin/macdeployqt"
						"/Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/build/install/lsl_Release/XDFBrowser/XDFBrowser.app"
						-verbose=1
					)
				
endif()

