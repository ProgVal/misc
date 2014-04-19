#!/bin/sh
xmodmap -e "keycode  10 = ampersand 1 ampersand 1 U2019 periodcentered dead_acute periodcentered ampersand 1 dead_acute periodcentered"
#xmodmap -e "keycode 13 = U2019 4 apostrophe 4 braceleft apostrophe braceleft"
xmodmap -e "keycode  59 = semicolon period semicolon period U2026 multiply U2026"
#xmodmap -e "keycode  59 = semicolon period semicolon period horizconnector multiply horizconnector multiply semicolon period horizconnector multiply"
xmodmap -e "keycode  52 = w W w W guillemotleft less guillemotleft"

xmodmap -e "keycode  61 = exclam section exclam section multiply dead_abovedot multiply"
xmodmap -e "keycode  58 = comma question comma question questiondown masculine questiondown masculine comma question questiondown masculine comma question questiondown masculine"
xmodmap -e "keycode  94 = less greater less greater U2014 U2014 U2014 U2014 less greater U2014 U2014 less greater U2014 U2014"

xmodmap -e "keycode  135 = "
