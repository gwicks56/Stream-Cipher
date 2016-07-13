# -*- coding: utf-8 -*-


from base64 import b64encode, b64decode

key1 = 11380312415897726212538720767584623938377542218843650885786488543557849920563944820657401556147072220807050423844611527817088743264179887246035449031879964033048917437051768727745163996083995699396309860629605332639267450328379289961205789359923142431676348109877819086396004913235006262427231898532203764657706261780748597526471127787542155628754978941021278802504747939847153450812209928520258539639347968927907337576400038705453704498741239631581573919339705649004208586949422810873621196157474272177586468236634536851618181572350294408509526514361027546939234421045026063811415872877733865949984217287267027217419
key = 4
p = 11



message = '{"created_at":"Thu May 14 14:37:57 +0000 2015","id":598859802400268289,"id_str":"598859802400268289","text":"Good morning! ♥","source":"<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>","truncated":false,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":73727137,"id_str":"73727137","name":"Amber Bruns✂","screen_name":"ColourQueenAB","location":"SAN ANTONIO, TEXAS","url":null,"description":"COLOUR Queen B. #Hair Stylist in the Making. I LOVE COLOR! By Any Means. Anything Is Possible.","protected":false,"verified":false,"followers_count":319,"friends_count":442,"listed_count":12,"favourites_count":378,"statuses_count":5247,"created_at":"Sat Sep 12 20:29:07 +0000 2009","utc_offset":-18000,"time_zone":"Central Time (US & Canada)","geo_enabled":true,"lang":"en","contributors_enabled":false,"is_translator":false,"profile_background_color":"000000","profile_background_image_url":"http://abs.twimg.com/images/themes/theme14/bg.gif","profile_background_image_url_https":"https://abs.twimg.com/images/themes/theme14/bg.gif","profile_background_tile":false,"profile_link_color":"0B4040","profile_sidebar_border_color":"000000","profile_sidebar_fill_color":"000000","profile_text_color":"000000","profile_use_background_image":false,"profile_image_url":"http://pbs.twimg.com/profile_images/490955924693995520/uY90KDh0_normal.jpeg","profile_image_url_https":"https://pbs.twimg.com/profile_images/490955924693995520/uY90KDh0_normal.jpeg","profile_banner_url":"https://pbs.twimg.com/profile_banners/73727137/1386261952","default_profile":false,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":{"id":"3df4f427b5a60fea","url":"https://api.twitter.com/1.1/geo/id/3df4f427b5a60fea.json","place_type":"city","name":"San Antonio","full_name":"San Antonio, TX","country_code":"US","country":"United States","bounding_box":{"type":"Polygon","coordinates":[[[-98.778559,29.141956],[-98.778559,29.693046],[-98.302744,29.693046],[-98.302744,29.141956]]]},"attributes":{}},"contributors":null,"retweet_count":0,"favorite_count":0,"entities":{"hashtags":[],"trends":[],"urls":[],"user_mentions":[],"symbols":[]},"favorited":false,"retweeted":false,"possibly_sensitive":false,"filter_level":"low","lang":"en","timestamp_ms":"1431614277826"}'
message2 = 'ZnlwaWQyeGpjbTluV0dGd0tqc25YV3B6S2s1bWVTUTVOU1U0Tmp3NU5EMDFNeWdxTlRreU5pb3hOekV4S2kwbllHWWtNRFkrT0R3OU9EMDVNREk2TXpVMlBEbzVQQ1VnYjI1Y2RIUjJLanNuUERzK01qWStPRFE2TlRVNU1EQXlNVDg1SmlRamNXeDZjaWc1SlVkcloyVWxaRzEwWkdwcFp5VW80NXlzSUNvb2NHaDFkbXRrSnpNZ09tc2piM0poYmp3bllYWnllamtvTDNCL2FIRjlaM1FrWUdodEsyeHVjbWR1YVd0bktHRnFiSE5xWUdZa0tuRmliRGtxYjJwdmJXcG1iSEFpT2x4MmJIMTJZM2dqWVc5MktFQnJiWEJwWTJjN0wyVTJJeWtyZG5SL2JXUmhjRzFsSnpOa1oyWndZaXdtWVc5YWUyZDJabnBZZEd0WGNuRm9kbk41WEc1a0pqSnZjR1Z1S2locWFWOTJiWEZwY0YxeVpWeDBkR1Y4ZEhaV2EySlZjSE55SmpKdmNHVnVLaWhxYVY5MmJYRnBjRjF5WlZ4eWMyRjZYbXh0SUR4a2RtdHNLQ3BvYTFad1kzcHZmbDl3WjE1d2VtZDBWV3BqWDNkOGN5Y3piSE5tYnlzaWJXWmVkMnh5YW5OY2MyOWJlMkozYkdkb1ZXMW1iV0VxTzJ0OGJtb21JWEp6WVhvalAzSWdiMjRoUFRjM1B6TXlPREV4SmlGdVpGdDdkWGNyT0NROU1EQXlNemt5TWlzdUpHUmlhbVVtTWlORVpHQmplQ05GY25GbWN1ZVZnQ1FtSVhSamRtMWthMVpzWjJkbUpUb21TMjVwWm5kMFczWmlaV3BKUXljbElHcGxZR1owYldkdkp6TWdWVXROSjBGS1hFNUxRRTBxS2xkQ1dFVmJJeWtyZDNSbUlUMXVjV1J0S1N0bVkzbGdkV2wwZkdocVp5QThLRUJJVEV0ZFV5VllkMk52YlNkQ0tpZ2lUV2hyZENwUWMzbG9ZWEp4S1d0b0tuZHZaU1JGWUc1Z2JHRWtJMDRnU0VkWFFDbEJTVVpNVlNFa1NuZ2xTR3gvS2s1aVlXcDdMeVZJYkg5K2EyNXVZeWhJZGlsU2FYbHdibUpvYlM4bkpTQjJlR3h6WldkOFpHRXJPR0JyYjNSbEtDcDNZSHRyWUdObVl5SStibUJwZW1jcUtHVm9iR2huZG1CN2NWbHBiSEp1Y0NvN05qZzdLaWhsZFdsaFptVjJWbUZwZjIxeklqNDhOVGNsSUdwamNITmxZRmRpYW54c2NpZzVOaklvS21ka2YyMXplR3B6WlhkWFltcDhiSElvT1RRM1BDUWpkbjFqY245d1luTmJhMjV3WjNZa01EWTFORE1rSTJaN1oyZCtabU5mWlh3alB5dFJaMzRqVkdWMEtEQTNLVEEyTURFK09qUS9JUzQ1TWpZNkl6VXdOREVqS1N0M2NtbGNhR1ppZTJSeEt6Z3JPenMzTURRa0kzRmdiMk5WZVdodVlTbzdKMHBuYUg1eFptd2tYR2hvYkNJdVgxQW5KaVJMWUd0b1ptY2pJU3NpWTIxdVdteHNaMmh2WW1RbU1uVjNmR2NxS0c5bWJtTXFPeWRzYkNRbUlXUnZhbnh6Ykd0M2NtVnhkRjloWm1CblpXZGlLRGxoWVdoN1pDa3JhM1ZWZDNWaGFudHRaSDF0ZENnNVlXRm9lMlFwSzNKMFpXVnViR0ZYWTJScWFXRjRiSEp1WUZkaWFtVnRkQ2c1SlRBME9ERTFPU0FxS0hOMWIySmhiV0JXWUdkcGFHQnlhMzF2WVZacmEydGtZbDl4ZW0wbk15QnVmbmQzT2lzbllHZDZMSEo5YW1wbkttdHVhQ1pyYTJ0a1luTXJmR2xnWkdkMUpYZHZaV2x0TURFbVlHRWtaRzVtSmlRamRYdHRZR052WWw5bWFXSnVibkJwZjIxalgyMWxZR0pzWFhONGIxaG9jSHh4ZGlzNEpHSjNjM0IzTWk0cWFHQjFKSGR3YVdsdkwyWm1ieWxqYm1abllYc3VjV0ZuYTI5d0tIUnNiV3hnT0RZcGFHUXBaMjF1SXlrcmNuUmxaVzVzWVZkalpHcHBZWGhzY201Z1YzVnNaV2NrTUdWbWJIZHRMU2Q1Y0dsc2FtdGxXMlJvYTJKZFpXVnZhSEltTWlNMVN6WTJQak1sTENaNGMycHZhMnB2WEhScFlHMWpaSHRkWkdWeFkyVjJWMkpxWlcxMEtEa2xNRFE0TVRVNUlDb29jM1Z2WW1GdFlGWnhiMjVtWldGMlYyZHNaVzVaYVd4cmIzWXFPeWM1TWpZNk16Y2lLQ3B4ZDJaa2IyWm1XSFJoY0hWYWFtMXFaWEVsT2lZNE1UVTVNallvTHlWd2RtZG5iR1ZuV1g5d1lsOW1hV0p1Ym5CcGYyMWpYMjFsWUdKc0lEeHNZbXR6WVNRamRYdHRZR052WWw5dFpXQmliRjF6ZUc4bE9pWmdkWEY1T0NrbGMyVnpLbngyYkdSbEtHbHNhaTkwZW01allHNWpWV3BxWVdOdGNpbzlPell6TmpJNU5qdzNQRG83UHo4Mk5UQXJmVmc4T1VsQ1lqTllibXQ2YkdSbExHeDZabUFpS0NweGQyWmtiMlptV0dscGFXWmdWbmQwWmx4dmRIQjRjaWN6SUc1K2QzZHpQaWN1ZFd0eEtINTBibTFqSm1KcVpDMTJlR3hoYVdodFhteGtZMkZ2Y0NnMFBUZzRNRHc3TkQ0MVBqTTlNVFF3T3pJcGYxbytNRTlNYVRWV2JHbDRibVpzS21KeFlHNGdLaWh6ZFc5aVlXMWdWbUJuWkcxaWNsdDljMmtyT0NSaWQzTndkekl1S25sZ2RTUjNjR2xwYnk5bVptOHBlbkZvWm0xa1pGcHJZMmhrWm5Wekt6OHlNanMxTnprMEtERTNNRGMzUHpNL1B6RWxMQ1pzWkdOb2QycCtYSGR5YTI1b2FXd2dQR3hpYTNOaEpDTmhiR1JuZjI5elgzUjZibU5nYm1OVmFtcGhZMjBqUDI5amFubG1LeUppWjIxcFpuVnZaR1FsT21wOWJXa2xJR0JsYjJ0dmMxZHpZSGgzWTNsM1dITmhablVuTTJ4elptOHJJbXBuZFd4dmEyVnJkMjV2YW5zalAyZDNhbVorS3lKamJXNG5NMnh6Wm04ckltZG5ibmR0YTJocmQySnpKakp2Y0dWdUtpaHphMkZuYlNNL2NpQnZiaUU5SWpkc1p6RnZOalE5WVRKaE1qaG5ZR2dnS2loMmRXd21NaU50ZlhaMmVUa29MMlY0YUN0OWRXOStkMkp5S210dWFDWXpLRHNzWUdWckoyaGhKakZpYkRkaE5EWS9ZekJvTkRac1ptWXVibnR1YXlzdUpIcHZabU5oVjNWOGVXY2tNQ0ZrYVhCeEl5a3JiR2RuWmlVNkpsdGdheWxEYUg1c2FXbHJLaTBuYjNkcVpseHBZV2x0SXo4clVXZGtJMFp1Y0dkdmJHWXVKbDViSlN3bWEyNXdaM1owYzF4a2IyQnRJejhyVjFVb0x5VmphMzF2Y1h0N0pEQWhVbTV0ZkdSaEtWRnlhM2RpY3lZa0kyZG1kMmh1YW1sblcycHVmU3M0ZlNoM2ZuQmhLanNuV1cxcWMyUm9iaVlrSTJabWJYUnVhbWxoY0cxeUp6TlpYVkV1UGpncVB6WTlQRGMvSmpFK0xqVThNRHc4TkZzbVdDbzVQQ1kyTWpFM016TXZOVGtxUGpnMk9UWXdWeTljTFQwd0x6WTVNREUrTnlzeVBTWTNQRG95TWp4ZUsxc3BNVGtyT2pJMFBUY3pMRFl4THpROU16OC9OVnBkV1hVdEoyaDJjbmhxWlhWd2JYSW5NM2w3ZHk4bFkydG1kWGRnWUhOK2JIVnpKakp2Y0dWdUtpaHhZblJ6YldSeFZtRnBmMjF6SWo0NExTZHZZM0JsY1c1MFlWZGlhbnhzY2lnNU55d21iVzl4WUhadmIzQWxPbjhxYVdSNmFuSnJaSFFpUGxOY0tTdDJkRzl0WTNNbU1scFlKU0J6ZUc5MElqNVRYQ2tyZDNWdmNWaHRZV1oxYkdac2RTZzVYRjBvS25KOFpHQnBabkFsT2w5VmZDa3JaR2Q4YkhWcGNHMWxKek5rWjJad1lpd21lbVJ4Zm1kamZtWmpJajV1WUdsNlp5b29jMmh6ZDJGamFYQmRkVzl0ZEdsd1lYZGdLemhnYTI5MFpTZ3FaMnhsZG1ONFhHdGxjbTF0SnpNZ2FtVjBKU3dtWkdCcmJpQThLR1pwSWlncWRXeGtaM1YrWW1wd1cyVnlKek1nTno0d05qWTFQRE15UGpvMFBDRjY='
message3 = '{'
message4 = 'fw=='
message5 = 'Znc9PQ=='
message6 = '♥'

def binary(i):
    if i == 0:
        return "0"
    s = ''
    while i:
        if i & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i >>= 1
    c = int(s)
    l = format(c, '008')
    return l

def msb(i):
    a = binary(i)
    b = a[0:8]
    c = int(b)
    l = format(c, '008')

    return l

def msb2(i):
    a = binary(i)
    b = a[0:8]
    c = int(b, 2)
    

    return c

print "msb test"
print msb2(13892949480140891204)

def parityWordChecksum(key):
    #assert(type(key) == type(1L))
    assert(key < (2 ** 2048))
    total_bits = 2048
    word_bits = 64

    

    mask = (1 << total_bits) - 1

    while total_bits > word_bits:
            total_bits >>= 1
            key ^= (key >> total_bits)
            mask >>= total_bits
            key &= mask
    return key

#print "parity checksum check"

#print parityWordChecksum(4)

def deriveSupplementaryKey(key, p):
    #assert(type(key) == type(1L))
    assert(type(p) == type(1))
    assert(key < (2 ** 2048))
    assert(p < (2 ** 64))

    subKey = key % p


    assert(type(subKey) == type(1) or type(subKey) == type(1L))
    return subKey

#other1 = deriveSupplementaryKey(key,a)
r0 = parityWordChecksum(key)
a = deriveSupplementaryKey(key, 3)
print "AAAA"
print a
b = deriveSupplementaryKey(key, 5)
print "BBB"
print b

def reset():
    global r0
    r0 = parityWordChecksum(key)


def updateShiftRegister():
    global r0
    r_new = (a*r0 +b) % p
    r0 = r_new
    
    


c = 'c'
#k = b64encode(c).decode('hex')
#print k
hello = "hellow world"
new = []
for x in range(len(hello)):
    new.append(hello[x])

#print new


print "msb check"
print msb(13892949480140891204)

print "special characters"
work = b64encode('♥')
print work
keys = [1]

parity = parityWordChecksum(key)
print "parity"
print parity
firstkey = (((a * parity) + b) % p)


print "first key"
print firstkey

keys[0] = parityWordChecksum(key)
#keys[0] = (((a * parityWordChecksum(key)) + b) % p)

for x in range(10000):
    keys.append((a * keys[x] + b) % p)
    
print "KEYS"
print keys[0]
print keys[1]
print keys[2]
print keys[3]
print keys[4]
print keys[5]
print keys[6]
print keys[7]
print keys[8]

#print keys





      

def encrypt3(msg):
    #print " Seperate XOR function Try"
    ciphertext = ""
    cipherb64 = ''
    new_b64 = ''
    
    #global r0

    for x in range(len(msg)):
        integer = ord(msg[x])
        binary_rep = binary(integer)
        cipher_binary = cipher(binary_rep)
        #print "cipher binary"
        #print cipher_binary
        
        cipher_char = chr(cipher_binary)
        #print cipher_char
        ciphertext = ciphertext + cipher_char
        now =  b64encode(cipher_char)
        cipherb64 = cipherb64 + now
    #print "ciphertext before b64"
    #print ciphertext
    #print "cipher base64"
    #print cipherb64
    #print "*************************************"
    ciphertext1 = b64encode(ciphertext)
    #print "ciphertext"
    #print ciphertext1
    #print "another now b64"
    another = b64encode(ciphertext1)
    #print another
    reset()
    return another
   
def decrypt3(msg):

    plaintext = ''
    
    #print "original message"
    #print msg
    #print "after one b64 decode"
    decode = b64decode(msg)
    
    #print decode
    #print "why cant i decode"
    decode2 = b64decode(decode)
    #print decode2
    #print "now to binary"
    for x in range(len(decode2)):
        #updateShiftRegister()
        integer = ord(decode2[x]) 
        #print integer
        binary_rep = binary(integer)
        # print binary_rep
        cipher_binary = cipher(binary_rep)
        #print "cipher_binary"
        #print cipher_binary
        cipher_char = chr(cipher_binary)
        #print cipher_char
        plaintext = plaintext + cipher_char
        now = b64encode(cipher_char)
        #print now

        
    print "plaintext next rest\n\n\n"
    return plaintext
    
    print "END OF DECRYPT\n\n\n"



def cipher(msg):
    global r0
    msb_num = msb(r0)
    cipher_binary = int(msg,2) ^ int(msb_num,2)
    updateShiftRegister()
    return cipher_binary
    
    

        


encrypted_message = encrypt3(message)
print encrypted_message
print "DECRYPT"
print "message 4\n\n"
print decrypt3(encrypted_message)
print msb(512)
print msb2(512)


