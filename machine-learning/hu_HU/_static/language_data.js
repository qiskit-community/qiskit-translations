/*
 * language_data.js
 * ~~~~~~~~~~~~~~~~
 *
 * This script contains the language-specific data used by searchtools.js,
 * namely the list of stopwords, stemmer, scorer and splitter.
 *
 * :copyright: Copyright 2007-2021 by the Sphinx team, see AUTHORS.
 * :license: BSD, see LICENSE for details.
 *
 */

var stopwords = ["a","abban","ahhoz","ahogy","ahol","aki","akik","akkor","alatt","amely","amelyek","amelyekben","amelyeket","amelyet","amelynek","ami","amikor","amit","amolyan","am\u00edg","annak","arra","arr\u00f3l","az","azok","azon","azonban","azt","azt\u00e1n","azut\u00e1n","azzal","az\u00e9rt","be","bel\u00fcl","benne","b\u00e1r","cikk","cikkek","cikkeket","csak","de","e","ebben","eddig","egy","egyes","egyetlen","egyik","egyre","egy\u00e9b","eg\u00e9sz","ehhez","ekkor","el","ellen","els\u0151","el\u00e9g","el\u0151","el\u0151sz\u00f6r","el\u0151tt","emilyen","ennek","erre","ez","ezek","ezen","ezt","ezzel","ez\u00e9rt","fel","fel\u00e9","hanem","hiszen","hogy","hogyan","igen","ill","ill.","illetve","ilyen","ilyenkor","ism\u00e9t","ison","itt","jobban","j\u00f3","j\u00f3l","kell","kellett","keress\u00fcnk","kereszt\u00fcl","ki","k\u00edv\u00fcl","k\u00f6z\u00f6tt","k\u00f6z\u00fcl","legal\u00e1bb","legyen","lehet","lehetett","lenne","lenni","lesz","lett","maga","mag\u00e1t","majd","meg","mellett","mely","melyek","mert","mi","mikor","milyen","minden","mindenki","mindent","mindig","mint","mintha","mit","mivel","mi\u00e9rt","most","m\u00e1r","m\u00e1s","m\u00e1sik","m\u00e9g","m\u00edg","nagy","nagyobb","nagyon","ne","nekem","neki","nem","nincs","n\u00e9ha","n\u00e9h\u00e1ny","n\u00e9lk\u00fcl","olyan","ott","pedig","persze","r\u00e1","s","saj\u00e1t","sem","semmi","sok","sokat","sokkal","szemben","szerint","szinte","sz\u00e1m\u00e1ra","tal\u00e1n","teh\u00e1t","teljes","tov\u00e1bb","tov\u00e1bb\u00e1","t\u00f6bb","ugyanis","utols\u00f3","ut\u00e1n","ut\u00e1na","vagy","vagyis","vagyok","valaki","valami","valamint","val\u00f3","van","vannak","vele","vissza","viszont","volna","volt","voltak","voltam","voltunk","\u00e1ltal","\u00e1ltal\u00e1ban","\u00e1t","\u00e9n","\u00e9ppen","\u00e9s","\u00edgy","\u00f6ssze","\u00fagy","\u00faj","\u00fajabb","\u00fajra","\u0151","\u0151k","\u0151ket"];


/* Non-minified version is copied as a separate JS file, is available */
BaseStemmer=function(){this.setCurrent=function(r){this.current=r;this.cursor=0;this.limit=this.current.length;this.limit_backward=0;this.bra=this.cursor;this.ket=this.limit};this.getCurrent=function(){return this.current};this.copy_from=function(r){this.current=r.current;this.cursor=r.cursor;this.limit=r.limit;this.limit_backward=r.limit_backward;this.bra=r.bra;this.ket=r.ket};this.in_grouping=function(r,t,i){if(this.cursor>=this.limit)return false;var s=this.current.charCodeAt(this.cursor);if(s>i||s<t)return false;s-=t;if((r[s>>>3]&1<<(s&7))==0)return false;this.cursor++;return true};this.in_grouping_b=function(r,t,i){if(this.cursor<=this.limit_backward)return false;var s=this.current.charCodeAt(this.cursor-1);if(s>i||s<t)return false;s-=t;if((r[s>>>3]&1<<(s&7))==0)return false;this.cursor--;return true};this.out_grouping=function(r,t,i){if(this.cursor>=this.limit)return false;var s=this.current.charCodeAt(this.cursor);if(s>i||s<t){this.cursor++;return true}s-=t;if((r[s>>>3]&1<<(s&7))==0){this.cursor++;return true}return false};this.out_grouping_b=function(r,t,i){if(this.cursor<=this.limit_backward)return false;var s=this.current.charCodeAt(this.cursor-1);if(s>i||s<t){this.cursor--;return true}s-=t;if((r[s>>>3]&1<<(s&7))==0){this.cursor--;return true}return false};this.eq_s=function(r){if(this.limit-this.cursor<r.length)return false;if(this.current.slice(this.cursor,this.cursor+r.length)!=r){return false}this.cursor+=r.length;return true};this.eq_s_b=function(r){if(this.cursor-this.limit_backward<r.length)return false;if(this.current.slice(this.cursor-r.length,this.cursor)!=r){return false}this.cursor-=r.length;return true};this.find_among=function(r){var t=0;var i=r.length;var s=this.cursor;var e=this.limit;var h=0;var u=0;var n=false;while(true){var c=t+(i-t>>>1);var a=0;var f=h<u?h:u;var l=r[c];var o;for(o=f;o<l[0].length;o++){if(s+f==e){a=-1;break}a=this.current.charCodeAt(s+f)-l[0].charCodeAt(o);if(a!=0)break;f++}if(a<0){i=c;u=f}else{t=c;h=f}if(i-t<=1){if(t>0)break;if(i==t)break;if(n)break;n=true}}do{var l=r[t];if(h>=l[0].length){this.cursor=s+l[0].length;if(l.length<4)return l[2];var v=l[3](this);this.cursor=s+l[0].length;if(v)return l[2]}t=l[1]}while(t>=0);return 0};this.find_among_b=function(r){var t=0;var i=r.length;var s=this.cursor;var e=this.limit_backward;var h=0;var u=0;var n=false;while(true){var c=t+(i-t>>1);var a=0;var f=h<u?h:u;var l=r[c];var o;for(o=l[0].length-1-f;o>=0;o--){if(s-f==e){a=-1;break}a=this.current.charCodeAt(s-1-f)-l[0].charCodeAt(o);if(a!=0)break;f++}if(a<0){i=c;u=f}else{t=c;h=f}if(i-t<=1){if(t>0)break;if(i==t)break;if(n)break;n=true}}do{var l=r[t];if(h>=l[0].length){this.cursor=s-l[0].length;if(l.length<4)return l[2];var v=l[3](this);this.cursor=s-l[0].length;if(v)return l[2]}t=l[1]}while(t>=0);return 0};this.replace_s=function(r,t,i){var s=i.length-(t-r);this.current=this.current.slice(0,r)+i+this.current.slice(t);this.limit+=s;if(this.cursor>=t)this.cursor+=s;else if(this.cursor>r)this.cursor=r;return s};this.slice_check=function(){if(this.bra<0||this.bra>this.ket||this.ket>this.limit||this.limit>this.current.length){return false}return true};this.slice_from=function(r){var t=false;if(this.slice_check()){this.replace_s(this.bra,this.ket,r);t=true}return t};this.slice_del=function(){return this.slice_from("")};this.insert=function(r,t,i){var s=this.replace_s(r,t,i);if(r<=this.bra)this.bra+=s;if(r<=this.ket)this.ket+=s};this.slice_to=function(){var r="";if(this.slice_check()){r=this.current.slice(this.bra,this.ket)}return r};this.assign_to=function(){return this.current.slice(0,this.limit)}};
HungarianStemmer=function(){var r=new BaseStemmer;var e=[["cs",-1,-1],["dzs",-1,-1],["gy",-1,-1],["ly",-1,-1],["ny",-1,-1],["sz",-1,-1],["ty",-1,-1],["zs",-1,-1]];var i=[["á",-1,1],["é",-1,2]];var a=[["bb",-1,-1],["cc",-1,-1],["dd",-1,-1],["ff",-1,-1],["gg",-1,-1],["jj",-1,-1],["kk",-1,-1],["ll",-1,-1],["mm",-1,-1],["nn",-1,-1],["pp",-1,-1],["rr",-1,-1],["ccs",-1,-1],["ss",-1,-1],["zzs",-1,-1],["tt",-1,-1],["vv",-1,-1],["ggy",-1,-1],["lly",-1,-1],["nny",-1,-1],["tty",-1,-1],["ssz",-1,-1],["zz",-1,-1]];var t=[["al",-1,1],["el",-1,1]];var s=[["ba",-1,-1],["ra",-1,-1],["be",-1,-1],["re",-1,-1],["ig",-1,-1],["nak",-1,-1],["nek",-1,-1],["val",-1,-1],["vel",-1,-1],["ul",-1,-1],["nál",-1,-1],["nél",-1,-1],["ból",-1,-1],["ról",-1,-1],["tól",-1,-1],["ül",-1,-1],["ből",-1,-1],["ről",-1,-1],["től",-1,-1],["n",-1,-1],["an",19,-1],["ban",20,-1],["en",19,-1],["ben",22,-1],["képpen",22,-1],["on",19,-1],["ön",19,-1],["képp",-1,-1],["kor",-1,-1],["t",-1,-1],["at",29,-1],["et",29,-1],["ként",29,-1],["anként",32,-1],["enként",32,-1],["onként",32,-1],["ot",29,-1],["ért",29,-1],["öt",29,-1],["hez",-1,-1],["hoz",-1,-1],["höz",-1,-1],["vá",-1,-1],["vé",-1,-1]];var u=[["án",-1,2],["én",-1,1],["ánként",-1,2]];var n=[["stul",-1,1],["astul",0,1],["ástul",0,2],["stül",-1,1],["estül",3,1],["éstül",3,3]];var f=[["á",-1,1],["é",-1,1]];var c=[["k",-1,3],["ak",0,3],["ek",0,3],["ok",0,3],["ák",0,1],["ék",0,2],["ök",0,3]];var l=[["éi",-1,1],["áéi",0,3],["ééi",0,2],["é",-1,1],["ké",3,1],["aké",4,1],["eké",4,1],["oké",4,1],["áké",4,3],["éké",4,2],["öké",4,1],["éé",3,2]];var o=[["a",-1,1],["ja",0,1],["d",-1,1],["ad",2,1],["ed",2,1],["od",2,1],["ád",2,2],["éd",2,3],["öd",2,1],["e",-1,1],["je",9,1],["nk",-1,1],["unk",11,1],["ánk",11,2],["énk",11,3],["ünk",11,1],["uk",-1,1],["juk",16,1],["ájuk",17,2],["ük",-1,1],["jük",19,1],["éjük",20,3],["m",-1,1],["am",22,1],["em",22,1],["om",22,1],["ám",22,2],["ém",22,3],["o",-1,1],["á",-1,2],["é",-1,3]];var k=[["id",-1,1],["aid",0,1],["jaid",1,1],["eid",0,1],["jeid",3,1],["áid",0,2],["éid",0,3],["i",-1,1],["ai",7,1],["jai",8,1],["ei",7,1],["jei",10,1],["ái",7,2],["éi",7,3],["itek",-1,1],["eitek",14,1],["jeitek",15,1],["éitek",14,3],["ik",-1,1],["aik",18,1],["jaik",19,1],["eik",18,1],["jeik",21,1],["áik",18,2],["éik",18,3],["ink",-1,1],["aink",25,1],["jaink",26,1],["eink",25,1],["jeink",28,1],["áink",25,2],["éink",25,3],["aitok",-1,1],["jaitok",32,1],["áitok",-1,2],["im",-1,1],["aim",35,1],["jaim",36,1],["eim",35,1],["jeim",38,1],["áim",35,2],["éim",35,3]];var m=[17,65,16,0,0,0,0,0,0,0,0,0,0,0,0,0,1,17,36,10,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1];var b=0;function _(){b=r.limit;r:{var i=r.cursor;e:{if(!r.in_grouping(m,97,369)){break e}i:while(true){var a=r.cursor;a:{if(!r.out_grouping(m,97,369)){break a}r.cursor=a;break i}r.cursor=a;if(r.cursor>=r.limit){break e}r.cursor++}i:{var t=r.cursor;a:{if(r.find_among(e)==0){break a}break i}r.cursor=t;if(r.cursor>=r.limit){break e}r.cursor++}b=r.cursor;break r}r.cursor=i;if(!r.out_grouping(m,97,369)){return false}e:while(true){i:{if(!r.in_grouping(m,97,369)){break i}break e}if(r.cursor>=r.limit){return false}r.cursor++}b=r.cursor}return true}function d(){if(!(b<=r.cursor)){return false}return true}function v(){var e;r.ket=r.cursor;e=r.find_among_b(i);if(e==0){return false}r.bra=r.cursor;if(!d()){return false}switch(e){case 1:if(!r.slice_from("a")){return false}break;case 2:if(!r.slice_from("e")){return false}break}return true}function g(){var e=r.limit-r.cursor;if(r.find_among_b(a)==0){return false}r.cursor=r.limit-e;return true}function j(){if(r.cursor<=r.limit_backward){return false}r.cursor--;r.ket=r.cursor;{var e=r.cursor-1;if(e<r.limit_backward){return false}r.cursor=e}r.bra=r.cursor;if(!r.slice_del()){return false}return true}function h(){r.ket=r.cursor;if(r.find_among_b(t)==0){return false}r.bra=r.cursor;if(!d()){return false}if(!g()){return false}if(!r.slice_del()){return false}if(!j()){return false}return true}function w(){r.ket=r.cursor;if(r.find_among_b(s)==0){return false}r.bra=r.cursor;if(!d()){return false}if(!r.slice_del()){return false}if(!v()){return false}return true}function z(){var e;r.ket=r.cursor;e=r.find_among_b(u);if(e==0){return false}r.bra=r.cursor;if(!d()){return false}switch(e){case 1:if(!r.slice_from("e")){return false}break;case 2:if(!r.slice_from("a")){return false}break}return true}function p(){var e;r.ket=r.cursor;e=r.find_among_b(n);if(e==0){return false}r.bra=r.cursor;if(!d()){return false}switch(e){case 1:if(!r.slice_del()){return false}break;case 2:if(!r.slice_from("a")){return false}break;case 3:if(!r.slice_from("e")){return false}break}return true}function y(){r.ket=r.cursor;if(r.find_among_b(f)==0){return false}r.bra=r.cursor;if(!d()){return false}if(!g()){return false}if(!r.slice_del()){return false}if(!j()){return false}return true}function C(){var e;r.ket=r.cursor;e=r.find_among_b(c);if(e==0){return false}r.bra=r.cursor;if(!d()){return false}switch(e){case 1:if(!r.slice_from("a")){return false}break;case 2:if(!r.slice_from("e")){return false}break;case 3:if(!r.slice_del()){return false}break}return true}function S(){var e;r.ket=r.cursor;e=r.find_among_b(l);if(e==0){return false}r.bra=r.cursor;if(!d()){return false}switch(e){case 1:if(!r.slice_del()){return false}break;case 2:if(!r.slice_from("e")){return false}break;case 3:if(!r.slice_from("a")){return false}break}return true}function B(){var e;r.ket=r.cursor;e=r.find_among_b(o);if(e==0){return false}r.bra=r.cursor;if(!d()){return false}switch(e){case 1:if(!r.slice_del()){return false}break;case 2:if(!r.slice_from("a")){return false}break;case 3:if(!r.slice_from("e")){return false}break}return true}function H(){var e;r.ket=r.cursor;e=r.find_among_b(k);if(e==0){return false}r.bra=r.cursor;if(!d()){return false}switch(e){case 1:if(!r.slice_del()){return false}break;case 2:if(!r.slice_from("a")){return false}break;case 3:if(!r.slice_from("e")){return false}break}return true}this.stem=function(){var e=r.cursor;_();r.cursor=e;r.limit_backward=r.cursor;r.cursor=r.limit;var i=r.limit-r.cursor;h();r.cursor=r.limit-i;var a=r.limit-r.cursor;w();r.cursor=r.limit-a;var t=r.limit-r.cursor;z();r.cursor=r.limit-t;var s=r.limit-r.cursor;p();r.cursor=r.limit-s;var u=r.limit-r.cursor;y();r.cursor=r.limit-u;var n=r.limit-r.cursor;S();r.cursor=r.limit-n;var f=r.limit-r.cursor;B();r.cursor=r.limit-f;var c=r.limit-r.cursor;H();r.cursor=r.limit-c;var l=r.limit-r.cursor;C();r.cursor=r.limit-l;r.cursor=r.limit_backward;return true};this["stemWord"]=function(e){r.setCurrent(e);this.stem();return r.getCurrent()}};
Stemmer = HungarianStemmer;



var splitChars = (function() {
    var result = {};
    var singles = [96, 180, 187, 191, 215, 247, 749, 885, 903, 907, 909, 930, 1014, 1648,
         1748, 1809, 2416, 2473, 2481, 2526, 2601, 2609, 2612, 2615, 2653, 2702,
         2706, 2729, 2737, 2740, 2857, 2865, 2868, 2910, 2928, 2948, 2961, 2971,
         2973, 3085, 3089, 3113, 3124, 3213, 3217, 3241, 3252, 3295, 3341, 3345,
         3369, 3506, 3516, 3633, 3715, 3721, 3736, 3744, 3748, 3750, 3756, 3761,
         3781, 3912, 4239, 4347, 4681, 4695, 4697, 4745, 4785, 4799, 4801, 4823,
         4881, 5760, 5901, 5997, 6313, 7405, 8024, 8026, 8028, 8030, 8117, 8125,
         8133, 8181, 8468, 8485, 8487, 8489, 8494, 8527, 11311, 11359, 11687, 11695,
         11703, 11711, 11719, 11727, 11735, 12448, 12539, 43010, 43014, 43019, 43587,
         43696, 43713, 64286, 64297, 64311, 64317, 64319, 64322, 64325, 65141];
    var i, j, start, end;
    for (i = 0; i < singles.length; i++) {
        result[singles[i]] = true;
    }
    var ranges = [[0, 47], [58, 64], [91, 94], [123, 169], [171, 177], [182, 184], [706, 709],
         [722, 735], [741, 747], [751, 879], [888, 889], [894, 901], [1154, 1161],
         [1318, 1328], [1367, 1368], [1370, 1376], [1416, 1487], [1515, 1519], [1523, 1568],
         [1611, 1631], [1642, 1645], [1750, 1764], [1767, 1773], [1789, 1790], [1792, 1807],
         [1840, 1868], [1958, 1968], [1970, 1983], [2027, 2035], [2038, 2041], [2043, 2047],
         [2070, 2073], [2075, 2083], [2085, 2087], [2089, 2307], [2362, 2364], [2366, 2383],
         [2385, 2391], [2402, 2405], [2419, 2424], [2432, 2436], [2445, 2446], [2449, 2450],
         [2483, 2485], [2490, 2492], [2494, 2509], [2511, 2523], [2530, 2533], [2546, 2547],
         [2554, 2564], [2571, 2574], [2577, 2578], [2618, 2648], [2655, 2661], [2672, 2673],
         [2677, 2692], [2746, 2748], [2750, 2767], [2769, 2783], [2786, 2789], [2800, 2820],
         [2829, 2830], [2833, 2834], [2874, 2876], [2878, 2907], [2914, 2917], [2930, 2946],
         [2955, 2957], [2966, 2968], [2976, 2978], [2981, 2983], [2987, 2989], [3002, 3023],
         [3025, 3045], [3059, 3076], [3130, 3132], [3134, 3159], [3162, 3167], [3170, 3173],
         [3184, 3191], [3199, 3204], [3258, 3260], [3262, 3293], [3298, 3301], [3312, 3332],
         [3386, 3388], [3390, 3423], [3426, 3429], [3446, 3449], [3456, 3460], [3479, 3481],
         [3518, 3519], [3527, 3584], [3636, 3647], [3655, 3663], [3674, 3712], [3717, 3718],
         [3723, 3724], [3726, 3731], [3752, 3753], [3764, 3772], [3774, 3775], [3783, 3791],
         [3802, 3803], [3806, 3839], [3841, 3871], [3892, 3903], [3949, 3975], [3980, 4095],
         [4139, 4158], [4170, 4175], [4182, 4185], [4190, 4192], [4194, 4196], [4199, 4205],
         [4209, 4212], [4226, 4237], [4250, 4255], [4294, 4303], [4349, 4351], [4686, 4687],
         [4702, 4703], [4750, 4751], [4790, 4791], [4806, 4807], [4886, 4887], [4955, 4968],
         [4989, 4991], [5008, 5023], [5109, 5120], [5741, 5742], [5787, 5791], [5867, 5869],
         [5873, 5887], [5906, 5919], [5938, 5951], [5970, 5983], [6001, 6015], [6068, 6102],
         [6104, 6107], [6109, 6111], [6122, 6127], [6138, 6159], [6170, 6175], [6264, 6271],
         [6315, 6319], [6390, 6399], [6429, 6469], [6510, 6511], [6517, 6527], [6572, 6592],
         [6600, 6607], [6619, 6655], [6679, 6687], [6741, 6783], [6794, 6799], [6810, 6822],
         [6824, 6916], [6964, 6980], [6988, 6991], [7002, 7042], [7073, 7085], [7098, 7167],
         [7204, 7231], [7242, 7244], [7294, 7400], [7410, 7423], [7616, 7679], [7958, 7959],
         [7966, 7967], [8006, 8007], [8014, 8015], [8062, 8063], [8127, 8129], [8141, 8143],
         [8148, 8149], [8156, 8159], [8173, 8177], [8189, 8303], [8306, 8307], [8314, 8318],
         [8330, 8335], [8341, 8449], [8451, 8454], [8456, 8457], [8470, 8472], [8478, 8483],
         [8506, 8507], [8512, 8516], [8522, 8525], [8586, 9311], [9372, 9449], [9472, 10101],
         [10132, 11263], [11493, 11498], [11503, 11516], [11518, 11519], [11558, 11567],
         [11622, 11630], [11632, 11647], [11671, 11679], [11743, 11822], [11824, 12292],
         [12296, 12320], [12330, 12336], [12342, 12343], [12349, 12352], [12439, 12444],
         [12544, 12548], [12590, 12592], [12687, 12689], [12694, 12703], [12728, 12783],
         [12800, 12831], [12842, 12880], [12896, 12927], [12938, 12976], [12992, 13311],
         [19894, 19967], [40908, 40959], [42125, 42191], [42238, 42239], [42509, 42511],
         [42540, 42559], [42592, 42593], [42607, 42622], [42648, 42655], [42736, 42774],
         [42784, 42785], [42889, 42890], [42893, 43002], [43043, 43055], [43062, 43071],
         [43124, 43137], [43188, 43215], [43226, 43249], [43256, 43258], [43260, 43263],
         [43302, 43311], [43335, 43359], [43389, 43395], [43443, 43470], [43482, 43519],
         [43561, 43583], [43596, 43599], [43610, 43615], [43639, 43641], [43643, 43647],
         [43698, 43700], [43703, 43704], [43710, 43711], [43715, 43738], [43742, 43967],
         [44003, 44015], [44026, 44031], [55204, 55215], [55239, 55242], [55292, 55295],
         [57344, 63743], [64046, 64047], [64110, 64111], [64218, 64255], [64263, 64274],
         [64280, 64284], [64434, 64466], [64830, 64847], [64912, 64913], [64968, 65007],
         [65020, 65135], [65277, 65295], [65306, 65312], [65339, 65344], [65371, 65381],
         [65471, 65473], [65480, 65481], [65488, 65489], [65496, 65497]];
    for (i = 0; i < ranges.length; i++) {
        start = ranges[i][0];
        end = ranges[i][1];
        for (j = start; j <= end; j++) {
            result[j] = true;
        }
    }
    return result;
})();

function splitQuery(query) {
    var result = [];
    var start = -1;
    for (var i = 0; i < query.length; i++) {
        if (splitChars[query.charCodeAt(i)]) {
            if (start !== -1) {
                result.push(query.slice(start, i));
                start = -1;
            }
        } else if (start === -1) {
            start = i;
        }
    }
    if (start !== -1) {
        result.push(query.slice(start));
    }
    return result;
}


