module DEC_7SEG(Hex_digit, segment_a, segment_b, segment_c,
                 segment_d, segment_e, segment_f, segment_g);
  input [3:0] Hex_digit;
  output segment_a, segment_b, segment_c, segment_d;
  output segment_e, segment_f, segment_g;
  reg [6:0] segment_data;
  always @(Hex_digit)
    case (Hex_digit)
      0: segment_data = 7'b1111110;
      1: segment_data = 7'b0110000;
      2: segment_data = 7'b1101101;
      3: segment_data = 7'b1111001;
      4: segment_data = 7'b0110011;
      5: segment_data = 7'b1011011;
      6: segment_data = 7'b1011111;
      7: segment_data = 7'b1110000;
      8: segment_data = 7'b1111111;
      9: segment_data = 7'b1111011;
      10: segment_data = 7'b1110111;
      11: segment_data = 7'b0011111;
      12: segment_data = 7'b1001110;
      13: segment_data = 7'b0111101;
      14: segment_data = 7'b1001111;
      15: segment_data = 7'b1000111;
      default: segment_data = 7'b0111110;
    endcase

  /* extract segment data bits and invert */
  /* LED driver circuit is inverted */
  wire segment_a = !segment_data[6];
  wire segment_b = !segment_data[5];
  wire segment_c = !segment_data[4];
  wire segment_d = !segment_data[3];
  wire segment_e = !segment_data[2];
  wire segment_f = !segment_data[1];
  wire segment_g = !segment_data[0];
endmodule
