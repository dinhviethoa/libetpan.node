# libEtPan! -- a mail stuff library
#
# Copyright (C) 2001-2013 - DINH Viet Hoa
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. Neither the name of the libEtPan! project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHORS AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHORS OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.

{
  "targets": [
    {
      "target_name": "etpan",
      'include_dirs': [
          'include',
          'include/libetpan',
          'deps/libetpan/src/data-types',
          'deps/libetpan/src/low-level/imf',
          'deps/libetpan/src/low-level/mime',
          'deps/libetpan/src/low-level/pop3',
          'deps/libetpan/src/low-level/imap',
          'deps/libetpan/src/low-level/smtp',
          "<!(node -e \"require('nan')\")",
      ],
      'defines': ['HAVE_CTYPE_H',
        'HAVE_ICONV',
        'HAVE_INTTYPES_H',
        'HAVE_IPV6',
        'HAVE_LIMITS_H',
        'HAVE_MEMORY_H',
        'HAVE_ARPA_INET_H',
        'HAVE_STDINT_H',
        'HAVE_STDLIB_H',
        'HAVE_STRING_H',
        'HAVE_SYS_MMAN_H',
        'HAVE_SYS_PARAM_H',
        'HAVE_SYS_SELECT_H',
        'HAVE_SYS_SOCKET_H',
        'HAVE_SYS_STAT_H',
        'HAVE_SYS_TYPES_H',
        'HAVE_UNISTD_H',
        'HAVE_ZLIB',
        'UNSTRICT_SYNTAX',
        'USE_SASL',
        'USE_SSL',
      ],
      'link_settings': {
        'libraries': [
          '-lz',
          '-lsasl2',
        ]
      },
      'sources': [ "src/libetpanjs.cc",
        "src/response.cc", "src/typesconv.cc",
        '<!@(find deps/libetpan/src/data-types -name *.c)',
        '<!@(find deps/libetpan/src/low-level/imf -name *.c)',
        '<!@(find deps/libetpan/src/low-level/mime -name *.c)',
        '<!@(find deps/libetpan/src/low-level/pop3 -name *.c)',
        '<!@(find deps/libetpan/src/low-level/imap -name *.c)',
        '<!@(find deps/libetpan/src/low-level/smtp -name *.c)',
      ]
    }
  ]
}
