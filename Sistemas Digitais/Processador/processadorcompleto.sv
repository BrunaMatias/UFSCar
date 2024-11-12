module processador_completo(a_in, b_in, clock, reset, pc, register_A, mdr_out, ir);

// memory_data = mdr
// memory_address = mar
// counter = pc 
// instruction_register = ir
// register_A = ac

input a_in, b_in;
input clock, reset;
output[7:0] pc;
output[15:0] register_A, mdr_out, ir;

reg[15:0] register_A, ir;
reg[7:0] pc; // aponta próxima ação
reg[3:0] state;

reg[7:0] mar; // memoria 8 bits 2^8 = 256 posições - liga na memória
reg memory_write;

parameter 	reset_pc = 0,
			fetch = 1,
			decode = 2,
			execute_add = 3,
			execute_jneg = 4,
			execute_store = 5,
			execute_store2 = 6,
			execute_store3 = 7,
			execute_load = 8,
			execute_jump = 9;
			
// fios de entradas e saídas para memória
wire[15:0] mdr;
assign mdr_out = mdr;
wire[15:0] mar_out = mar; 
wire memory_write_out = memory_write;

always@(posedge clock or posedge reset)
	begin
		if(reset)
			state = reset_pc; // parâmetro diz que ponteiro (pc) =  0 
		else
		
			case(state)
				reset_pc:
					begin 
						// limpa valores para iniciar processador
						pc = 8'b00000000; 
						register_A = 16'b0000000000000000;
						state = fetch;
					end
					
					fetch:
							begin
								ir = mdr;
								pc = pc + 1;
								state = decode;
							end
							
					decode:
						begin
							case(ir[15:8])				
								8'b00000000:
								state = execute_add;								
								8'b00000001:
									state = execute_store;
								8'b00000010:
									state = execute_load;
								8'b00000011:
									state = execute_jneg;
								8'b00000100:
									state = execute_store;
								8'b00000101:
									state = execute_store2;
								8'b00000110:
									state = execute_store3;
								8'b00000111:
									state = execute_load;
								8'b00001000:
									state = execute_jump;
				
								default:
									state = fetch;
							endcase
						end
						
					execute_add:
							begin
								register_A = register_A + mdr;
								state = fetch;
							end
					
					execute_store:
							begin
								state = execute_store2;
							end
							
					execute_store2:
							begin
								state = execute_store3;
							end
					
					execute_load: 
							begin
								register_A = mdr;
								state = execute_jneg;
								state = fetch;
							end
							
					execute_jump: 
							begin
								pc = ir[7:0];
								state = fetch;
							end
							
					execute_jneg: 
							begin 
								if (register_A < 0)
									state = execute_jump;
								if(register_A >= 0)
									pc = pc + 1;
							end
							
					default: 
							begin
								state = fetch;
							end
					endcase
	end
		
		always@(state or pc or ir)
			begin 
					case(state)
						reset_pc: mar = 8'h 00;
						fetch: mar = pc;
						decode: mar = ir[7:0];
						execute_add: mar = pc;
						execute_store: mar = ir[7:0];
						execute_store2: mar = pc;
						execute_load : mar = pc;
						execute_jump: mar = ir[7:0];
						
						default : mar = pc;
					endcase
					case(state)	
						execute_store: memory_write = 1'b 1;
						default: memory_write = 1'b 0;
					endcase
			end
endmodule