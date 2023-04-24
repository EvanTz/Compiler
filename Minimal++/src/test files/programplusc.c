#include <stdio.h>
int main()
{
 int var1,var2,var3,var4,T_1,T_2,T_3,T_4,T_5,T_6,T_7,T_8,T_9,T_10;
 L_1:
 L_2: printf("var1 input: ");
 scanf("%d",&var1);    //101: inp,var1,_,_
 L_3: printf("var2 input: ");
 scanf("%d",&var2);    //102: inp,var2,_,_
 L_4: if (var1<var2) goto L_6;    //103: <,var1,var2,105
 L_5: goto L_20;    //104: jump,_,_,119
 L_6: if (var1<2) goto L_8;    //105: <,var1,2,107
 L_7: goto L_13;    //106: jump,_,_,112
 L_8: if (var2>4) goto L_10;    //107: >,var2,4,109
 L_9: goto L_13;    //108: jump,_,_,112
 L_10: T_1=0-32767;    //109: -,0,32767,T_1
 L_11: printf("output T_1: %d\n",T_1);    //110: out,T_1,_,_
 L_12: goto L_14;    //111: jump,_,_,113
 L_13: printf("output 32767: %d\n",32767);    //112: out,32767,_,_
 L_14: T_2=var1+var2;    //113: +,var1,var2,T_2
 L_15: var3=T_2;    //114: :=,T_2,_,var3
 L_16: printf("output var3: %d\n",var3);    //115: out,var3,_,_
 L_17: T_3=1+var2;    //116: +,1,var2,T_3
 L_18: var1=T_3;    //117: :=,T_3,_,var1
 L_19: goto L_4;    //118: jump,_,_,103
 L_20: printf("output var3: %d\n",var3);    //119: out,var3,_,_
 L_21: if (var3>1) goto L_23;    //120: >,var3,1,122
 L_22: goto L_27;    //121: jump,_,_,126
 L_23: printf("output var3: %d\n",var3);    //122: out,var3,_,_
 L_24: T_4=var3-1;    //123: -,var3,1,T_4
 L_25: var3=T_4;    //124: :=,T_4,_,var3
 L_26: goto L_21;    //125: jump,_,_,120
 L_27: if (var3==1) goto L_29;    //126: =,var3,1,128
 L_28: goto L_35;    //127: jump,_,_,134
 L_29: T_5=var3+var1;    //128: +,var3,var1,T_5
 L_30: T_6=T_5+var2;    //129: +,T_5,var2,T_6
 L_31: printf("output T_6: %d\n",T_6);    //130: out,T_6,_,_
 L_32: T_7=var3-1;    //131: -,var3,1,T_7
 L_33: var3=T_7;    //132: :=,T_7,_,var3
 L_34: goto L_21;    //133: jump,_,_,120
 L_35: T_8=var3-10;    //134: -,var3,10,T_8
 L_36: var3=T_8;    //135: :=,T_8,_,var3
 L_37: printf("output var3: %d\n",var3);    //136: out,var3,_,_
 L_38: printf("var4 input: ");
 scanf("%d",&var4);    //137: inp,var4,_,_
 L_39: if (var4<=var3) goto L_43;    //138: <=,var4,var3,142
 L_40: goto L_41;    //139: jump,_,_,140
 L_41: if (var4>6) goto L_43;    //140: >,var4,6,142
 L_42: goto L_48;    //141: jump,_,_,147
 L_43: T_9=0-var4;    //142: -,0,var4,T_9
 L_44: printf("output T_9: %d\n",T_9);    //143: out,T_9,_,_
 L_45: T_10=0-var4;    //144: -,0,var4,T_10
 L_46: var4=T_10;    //145: :=,T_10,_,var4
 L_47: goto L_49;    //146: jump,_,_,148
 L_48: printf("output var4: %d\n",var4);    //147: out,var4,_,_
 L_49: {}
}
