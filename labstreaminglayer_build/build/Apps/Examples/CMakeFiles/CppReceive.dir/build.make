# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /Applications/CMake.app/Contents/bin/cmake

# The command to remove a file.
RM = /Applications/CMake.app/Contents/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/build

# Include any dependencies generated for this target.
include Apps/Examples/CMakeFiles/CppReceive.dir/depend.make

# Include the progress variables for this target.
include Apps/Examples/CMakeFiles/CppReceive.dir/progress.make

# Include the compile flags for this target's objects.
include Apps/Examples/CMakeFiles/CppReceive.dir/flags.make

Apps/Examples/CMakeFiles/CppReceive.dir/CppReceive.cpp.o: Apps/Examples/CMakeFiles/CppReceive.dir/flags.make
Apps/Examples/CMakeFiles/CppReceive.dir/CppReceive.cpp.o: ../Apps/Examples/CppReceive.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object Apps/Examples/CMakeFiles/CppReceive.dir/CppReceive.cpp.o"
	cd /Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/build/Apps/Examples && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/CppReceive.dir/CppReceive.cpp.o -c /Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/Apps/Examples/CppReceive.cpp

Apps/Examples/CMakeFiles/CppReceive.dir/CppReceive.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/CppReceive.dir/CppReceive.cpp.i"
	cd /Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/build/Apps/Examples && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/Apps/Examples/CppReceive.cpp > CMakeFiles/CppReceive.dir/CppReceive.cpp.i

Apps/Examples/CMakeFiles/CppReceive.dir/CppReceive.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/CppReceive.dir/CppReceive.cpp.s"
	cd /Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/build/Apps/Examples && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/Apps/Examples/CppReceive.cpp -o CMakeFiles/CppReceive.dir/CppReceive.cpp.s

Apps/Examples/CMakeFiles/CppReceive.dir/CppReceive.cpp.o.requires:

.PHONY : Apps/Examples/CMakeFiles/CppReceive.dir/CppReceive.cpp.o.requires

Apps/Examples/CMakeFiles/CppReceive.dir/CppReceive.cpp.o.provides: Apps/Examples/CMakeFiles/CppReceive.dir/CppReceive.cpp.o.requires
	$(MAKE) -f Apps/Examples/CMakeFiles/CppReceive.dir/build.make Apps/Examples/CMakeFiles/CppReceive.dir/CppReceive.cpp.o.provides.build
.PHONY : Apps/Examples/CMakeFiles/CppReceive.dir/CppReceive.cpp.o.provides

Apps/Examples/CMakeFiles/CppReceive.dir/CppReceive.cpp.o.provides.build: Apps/Examples/CMakeFiles/CppReceive.dir/CppReceive.cpp.o


# Object files for target CppReceive
CppReceive_OBJECTS = \
"CMakeFiles/CppReceive.dir/CppReceive.cpp.o"

# External object files for target CppReceive
CppReceive_EXTERNAL_OBJECTS =

Apps/Examples/CppReceive: Apps/Examples/CMakeFiles/CppReceive.dir/CppReceive.cpp.o
Apps/Examples/CppReceive: Apps/Examples/CMakeFiles/CppReceive.dir/build.make
Apps/Examples/CppReceive: LSL/liblsl/liblsl64.1.4.0.dylib
Apps/Examples/CppReceive: Apps/Examples/CMakeFiles/CppReceive.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable CppReceive"
	cd /Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/build/Apps/Examples && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/CppReceive.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
Apps/Examples/CMakeFiles/CppReceive.dir/build: Apps/Examples/CppReceive

.PHONY : Apps/Examples/CMakeFiles/CppReceive.dir/build

Apps/Examples/CMakeFiles/CppReceive.dir/requires: Apps/Examples/CMakeFiles/CppReceive.dir/CppReceive.cpp.o.requires

.PHONY : Apps/Examples/CMakeFiles/CppReceive.dir/requires

Apps/Examples/CMakeFiles/CppReceive.dir/clean:
	cd /Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/build/Apps/Examples && $(CMAKE_COMMAND) -P CMakeFiles/CppReceive.dir/cmake_clean.cmake
.PHONY : Apps/Examples/CMakeFiles/CppReceive.dir/clean

Apps/Examples/CMakeFiles/CppReceive.dir/depend:
	cd /Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer /Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/Apps/Examples /Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/build /Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/build/Apps/Examples /Users/futa/Documents/RESEARCH/sleep_eeg/labstreaminglayer/build/Apps/Examples/CMakeFiles/CppReceive.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : Apps/Examples/CMakeFiles/CppReceive.dir/depend

