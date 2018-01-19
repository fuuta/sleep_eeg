#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "lslboost" for configuration "Release"
set_property(TARGET lslboost APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(lslboost PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/LSL/lib/liblslboost.a"
  )

list(APPEND _IMPORT_CHECK_TARGETS lslboost )
list(APPEND _IMPORT_CHECK_FILES_FOR_lslboost "${_IMPORT_PREFIX}/LSL/lib/liblslboost.a" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
