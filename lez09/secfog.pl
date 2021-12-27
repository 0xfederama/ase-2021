% Inputs OpA id, A id 
% Outputs secure deployment D of A
secFog(OpA, A, D) :-
    app(A, L),
    deployment(OpA, L, D).

deployment(_, [], []). % all components are placed
deployment(OpA, [C|Cs], [d(C,N,OpN)|D]) :-
    node(N, OpN), % N is a node of OpN
    securityRequirements(C, N), % C is secure on N
    trusts2(OpA, OpN), % OpA trusts OpN
    deployment(OpA, Cs, D).

% transitive closure of trust network
trusts(X,X). % X trusts itself
trusts2(A,B) :-
    trusts(A,B). % A trusts B directly
trusts2(A,B) :-
    trusts(A,C),   % A trusts C that...
    trusts2(C,B).  % ... trusts B (in)directly

% App declaration + sec requirements
app(weatherApp, [weatherMonitor]).
securityRequirements(weatherMonitor, N) :-
    (anti_tampering(N); access_control(N)),
    (wireless_security(N); iot_data_encryption(N)).

% Node Descriptors
node(cloud, cloudOp).
0.99::anti_tampering(cloud).
0.99::access_control(cloud).
0.99::iot_data_encryption(cloud).

node(edge, edgeOp).
0.8::anti_tampering(edge).
0.9::wireless_security(edge).
0.9::iot_data_encryption(edge).

% trust network
%%% trust relations declared by appOp
.9::trusts(appOp, edgeOp).
.9::trusts(appOp, ispOp).
%%% trust relations declared by edgeOp
.7::trusts(edgeOp, cloudOp1).
.8::trusts(edgeOp, cloudOp2).
%%% trust relation declared by cloudOp1
.8::trusts(cloudOp1, cloudOp2).
%%% trust relation declared by cloudOp2
.2::trusts(cloudOp2, cloudOp).
%%% trust relations declared by ispOp
.8::trusts(ispOp, cloudOp).
.6::trusts(ispOp, edgeOp).

% problog <filename>.{pl,pro}
query(secFog(appOp, weatherApp, D)).
