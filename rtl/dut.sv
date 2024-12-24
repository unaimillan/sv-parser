
module test_mult_cocotb  #(
    parameter int FIX_BW_0          = 9,    // Inputs: a, b
    parameter int PNT_POS_0         = 7,
    parameter int FIX_BW_1          = 9,    // Power: a**2, b**2
    parameter int PNT_POS_1         = 7
) (
    input  logic [FIX_BW_0-1:0] inp,
    output logic [FIX_BW_1-1:0] out
);

    localparam int ACC_BW_1 = FIX_BW_0 * 2;
    logic [ACC_BW_1-1:0] acc;

    assign acc = inp * inp;

    localparam int MDPNT_1  = (PNT_POS_0 * 2) - 1;
    localparam int INT_BW_1 = FIX_BW_1 - PNT_POS_1;

    assign out = { acc[MDPNT_1+1 +: INT_BW_1], acc[MDPNT_1 -: PNT_POS_1] };

endmodule

