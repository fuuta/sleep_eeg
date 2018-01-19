
#ifndef LIBLSL_CPP_API_H
#define LIBLSL_CPP_API_H

#ifdef LSL_STATIC_DEFINE
#  define LIBLSL_CPP_API
#  define LSL_NO_EXPORT
#else
#  ifndef LIBLSL_CPP_API
#    ifdef lsl_EXPORTS
        /* We are building this library */
#      define LIBLSL_CPP_API __attribute__((visibility("default")))
#    else
        /* We are using this library */
#      define LIBLSL_CPP_API __attribute__((visibility("default")))
#    endif
#  endif

#  ifndef LSL_NO_EXPORT
#    define LSL_NO_EXPORT __attribute__((visibility("hidden")))
#  endif
#endif

#ifndef LSL_DEPRECATED
#  define LSL_DEPRECATED __attribute__ ((__deprecated__))
#endif

#ifndef LSL_DEPRECATED_EXPORT
#  define LSL_DEPRECATED_EXPORT LIBLSL_CPP_API LSL_DEPRECATED
#endif

#ifndef LSL_DEPRECATED_NO_EXPORT
#  define LSL_DEPRECATED_NO_EXPORT LSL_NO_EXPORT LSL_DEPRECATED
#endif

#if 0 /* DEFINE_NO_DEPRECATED */
#  ifndef LSL_NO_DEPRECATED
#    define LSL_NO_DEPRECATED
#  endif
#endif

#endif
