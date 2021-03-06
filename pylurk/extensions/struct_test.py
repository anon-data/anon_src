from tls12_struct import *

#testing client_hello
clt_h = \
{'client_version': {'major': 'TLS12M', 'minor': 'TLS12m'}, 'random':
{'gmt_unix_time': b'[|\x89\x9c', 'random': b'V{\xe5\xcd\xd8B\xc0\x80$4s\xf0\x1e\xc4o/4<\xb7#\xa0Z3\x95\x94\xa2\x1e\x89'}, 'session_id': b'\xe1/\xb4\xa7R\xc5\x03\xb3\t\xccH\x97\xf7\x9fnw\x1d@f$\xd7\x8an\xfdO\x85\x82\xe9\xe1\xf5\xd1\x83', 'cipher_suites': ['TLS_RSA_WITH_AES_128_GCM_SHA256', 'TLS_RSA_WITH_AES_256_GCM_SHA384'], 'compression_methods': ['null'], 'extensions': [{'extension_type': 'extended_master_secret', 'extension_data':  b''}]}

dict_session_id = clt_h['session_id' ]
bytes_session_id = SessionID.build( dict_session_id )
session_id = SessionID.parse( bytes_session_id )
print("session_id (bytes): %s\n session_id: %s"%(bytes_session_id, session_id ))

dict_cipher_suites = clt_h['cipher_suites' ]
bytes_cipher_suites = CipherSuites.build( dict_cipher_suites )
cipher_suites = CipherSuites.parse( bytes_cipher_suites )
print("cipher_suites (bytes): %s\n cipher_suites: %s"%(bytes_cipher_suites, cipher_suites ))

dict_extensions = clt_h[ 'extensions' ]
bytes_ext = Extensions.build(dict_extensions )
ext = Extensions.parse( bytes_ext )
print("extensions (bytes): %s\n extensions: %s"%(bytes_ext, ext ))

bytes_clt_h = ClientHello.build( clt_h )
clt_h = ClientHello.parse( bytes_clt_h )
print("bytes_clt_h (bytes): %s\n clt_h: %s"%(bytes_clt_h, clt_h ))

bytes_h_clt = Handshake.build( { 'msg_type' : 'client_hello', 'body' : clt_h } )
print("handshake client hello bytes: %s\n Handshake client hello : %s"%(bytes_h_clt, Handshake.parse( bytes_h_clt ) ))

#testing server_hello

#testing certificate
print( ASN1Cert.parse( b'\x00\x00\x01\xff' ) )
print( ASN1Cert.build( b'\xff') )

print( Certificate.build( [ b'\xff' ] ) )
print( Certificate.parse( b'\x00\x00\x04\x00\x00\x01\xff' )) 

print( Certificate.build( [ b'\xff', b'\xee' ] ) )
print( Certificate.parse( b'\x00\x00\x08\x00\x00\x01\xff\x00\x00\x01\xee'  ) )

print(" Testing Hanshake Message for Certificate") 
hs_certificate = { 'msg_type': 'certificate', \
                'body': [ b'\xff', b'\xee' ] }
hd_bytes = Handshake.build( hs_certificate ) 
print("bytes: %s\n dict: %s"%(hd_bytes, Handshake.parse( hd_bytes) ))

hs_certificate = {'msg_type': 'certificate', 'body': [b'0\x82\x03f0\x82\x02N\xa0\x03\x02\x01\x02\x02\x14nU\xc1o\xcb\x8d \x99\x14\xf2\x08\xcb\xb6\xc2y\xe4\x86_PH0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x0b\x05\x000\\1\x0b0\t\x06\x03U\x04\x06\x13\x02CA1\x0b0\t\x06\x03U\x04\x08\x0c\x02QC1\x110\x0f\x06\x03U\x04\x07\x0c\x08Montreal1\x130\x11\x06\x03U\x04\n\x0c\nMy Company1\x180\x16\x06\x03U\x04\x03\x0c\x0fwww.example.com0 \x17\r180508223907Z\x18\x0f21180414223907Z0\\1\x0b0\t\x06\x03U\x04\x06\x13\x02CA1\x0b0\t\x06\x03U\x04\x08\x0c\x02QC1\x110\x0f\x06\x03U\x04\x07\x0c\x08Montreal1\x130\x11\x06\x03U\x04\n\x0c\nMy Company1\x180\x16\x06\x03U\x04\x03\x0c\x0fwww.example.com0\x82\x01"0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x01\x05\x00\x03\x82\x01\x0f\x000\x82\x01\n\x02\x82\x01\x01\x00\xc0\x02\xe0\xd5\xe7\x17\xfe\xcf\x04>\xba\x16\xeb\xb289-\xef$\xbc\xf4TL\xcdQ(\xc6\x07\x8cwU\xec\x82%\xae\x1d\x01Y\x86\xa7\x9b\t\x18\x13\xb3\x15\xcaTw\n\x12\xc4\xb3L3\xbd\xc1\xe2\xaa@\x197\xd6l\x07\x8f\xc4\x82\xa7\xb1\xa5\xc07\xeb\x1b#\x8b4\x16]\xdf\x87\x94\xdd\xa8\xa7\xb9YO\xda\xc9\x02\x19\x06\x7f\xb4\x81\xce"+b\xec|\xa9\x95\xf20#\x97A\x19R<\xfd>\xf3\xad\xd6\xe6\xa4C\x13\r\xb9\xc8\x19\x17L\x94\xc7\xd8\xb8\xdd \xf6\xe6\xa3\xdfv\xdf\x0bH\xf5XF\xa0\x83\xc7P\x00\xed\xd2L\x83\xc4c\x93\x15\x83\x0c2\xec3,\x97U\x8c\x03\xef\xf1\xc0\xa8\xb7\x94\xfeVg\\.\xd1X\xc6\xb4\xc1\x97\x94\n\xa8F\xcd\xeb@.\xf3\x81\t\x8d\xb6@t\x9e,l\xbf\x01c\xd6\xcf\xef\x01\x91\x9e\xec\xca\xc7\x96\xde\x03\xb6\xe8\xe1Z816!$K\x9f\xfa\xe2<\x964\xd3\xce\xf5\x0f*Z\x94\x01\xb39\xb5ea\nA\xab>%\x93\xa2 \x17\x02\x03\x01\x00\x01\xa3\x1e0\x1c0\x1a\x06\x03U\x1d\x11\x04\x130\x11\x82\x0fwww.example.com0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x0b\x05\x00\x03\x82\x01\x01\x00AX\xda\x85\xfb\x06\xb0\x1a\xf7\x17\x01\x0b\xe8k\xf1i8G\xfb\xea\xe8n}kc\x91\xb5W-\xc9\xbc"\x06@gx\xd6\xbe@Gg>\x90+\x03\x83\x9es&q\x8f\x98\xf0m`[\xb9\x1e\xe0\r\x8c9\x12\rB^\xe3\xf0\x08z\x8a\xf3cl\x96v\x17\xb4\x1d\x98\xd12A7$|Y\x89\x96j?\x16\x85\xf8\xfc\xbf\xf4B\x89\x81\x01\xdb\xa3S\xe4\xcc7\xeb\x1b!\xdc`\x7f\x13U\x8e\xdeX\xec&\x1b\x00\xb7\xad\xccK\x01\x131\xc8Y,\xde\xef\xe6G\x98)\x1c\xe8\x1f\xf1\xfe\xc5\xf38tT#?\x9bl\x1bzwd\xdf\x87\x12\n=sBQ\x1f]|\x94\x9c!\xb1\x8c\xbd#\x01\xe4\xda\xb9\x17\xe6\xa8%\x8f9|\x07\xcb\xbc5\xc9KE\x8c\xf8\x1c\xc6VT\x900\xfdz\xaa\xef\xe8|\xd3z\xbd%-\xf7\xe8\xa3\xd3\xe6\x90\xf0\xc1\xc2\xf6`\xaf\x8f\xbf\x93y}-\xc45B3\x0el\x84 \x98S.\xf2xh\x1d\x8fU\x95y\xe9\xa4\xc8\xde\x82\xe0B ']}

hd_bytes = Handshake.build( hs_certificate ) 
#print("bytes: %s\n dict: %s"%(hd_bytes, Handshake.parse( hd_bytes) ))


#cert_bytes = Certificate.build( [{  b'\x00' }, {\b'\x01' }] ) 
#Certificate.parse(cert_bytes)

#testing server_hello_done
#ServerHelloDone.parse( ServerHelloDone.build())

# testing client_key_exchange


#testing handshake_messages

print("Testing Typed Certificate")

tcert = { 'certificate_type' : "x509", 'certificate_data' : b'\xff' } 
print( TypedCertificate.build( tcert ))

print(TypedCertificateList.build( [ tcert ] ) )
