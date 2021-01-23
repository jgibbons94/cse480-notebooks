
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = b'O\xbbl\x16\xa6\x04\xe5\x8di\x96\xdb\xe5\x07\xd4\x8a|'
    
_lr_action_items = {'error':([0,],[2,]),'DFA':([0,],[3,]),'NFA':([0,],[4,]),'PDA':([0,],[5,]),'TM':([0,],[6,]),'$end':([1,2,7,8,10,11,12,13,14,26,27,34,],[0,-1,-2,-6,-9,-3,-4,-5,-7,-10,-8,-11,]),'ID':([3,4,5,6,8,10,15,22,23,24,25,26,27,31,32,33,34,],[10,10,10,10,10,-9,19,10,19,19,19,-10,-8,10,19,19,-11,]),'COLON':([9,10,],[15,-9,]),'COMMA':([10,18,19,20,21,26,30,],[-9,24,-15,-16,-17,31,33,]),'EPS':([15,23,24,25,32,33,],[20,20,20,20,20,20,]),'BLANK':([15,23,24,25,32,33,],[21,21,21,21,21,21,]),'ARROW':([16,17,18,19,20,21,28,35,36,],[22,-12,-14,-15,-16,-17,-13,-18,-19,]),'OR':([17,18,19,20,21,35,36,],[23,-14,-15,-16,-17,-18,-19,]),'SEMICOLON':([18,19,20,21,29,],[25,-15,-16,-17,32,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'md':([0,],[1,]),'lines':([3,4,5,6,8,],[7,11,12,13,14,]),'one_line':([3,4,5,6,8,],[8,8,8,8,8,]),'state':([3,4,5,6,8,22,31,],[9,9,9,9,9,26,26,]),'labels':([15,23,],[16,28,]),'one_label':([15,23,],[17,17,]),'ID_or_EPS_or_B':([15,23,24,25,32,33,],[18,18,29,30,35,36,]),'states':([22,31,],[27,34,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> md","S'",1,None,None,None),
  ('md -> error','md',1,'p_you_are_hosed','../jove/Def_md2mc.py',461),
  ('md -> DFA lines','md',2,'p_dfa_md','../jove/Def_md2mc.py',468),
  ('md -> NFA lines','md',2,'p_nfa_md','../jove/Def_md2mc.py',481),
  ('md -> PDA lines','md',2,'p_pda_md','../jove/Def_md2mc.py',487),
  ('md -> TM lines','md',2,'p_tm_md','../jove/Def_md2mc.py',499),
  ('lines -> one_line','lines',1,'p_lines1','../jove/Def_md2mc.py',515),
  ('lines -> one_line lines','lines',2,'p_lines2','../jove/Def_md2mc.py',519),
  ('one_line -> state COLON labels ARROW states','one_line',5,'p_one_line','../jove/Def_md2mc.py',525),
  ('state -> ID','state',1,'p_state','../jove/Def_md2mc.py',543),
  ('states -> state','states',1,'p_states1','../jove/Def_md2mc.py',547),
  ('states -> state COMMA states','states',3,'p_states2','../jove/Def_md2mc.py',551),
  ('labels -> one_label','labels',1,'p_labels1','../jove/Def_md2mc.py',555),
  ('labels -> one_label OR labels','labels',3,'p_labels2','../jove/Def_md2mc.py',559),
  ('one_label -> ID_or_EPS_or_B','one_label',1,'p_one_label1','../jove/Def_md2mc.py',576),
  ('ID_or_EPS_or_B -> ID','ID_or_EPS_or_B',1,'p_ID_or_EPS_or_B','../jove/Def_md2mc.py',580),
  ('ID_or_EPS_or_B -> EPS','ID_or_EPS_or_B',1,'p_ID_or_EPS_or_B','../jove/Def_md2mc.py',581),
  ('ID_or_EPS_or_B -> BLANK','ID_or_EPS_or_B',1,'p_ID_or_EPS_or_B','../jove/Def_md2mc.py',582),
  ('one_label -> ID_or_EPS_or_B COMMA ID_or_EPS_or_B SEMICOLON ID_or_EPS_or_B','one_label',5,'p_one_label2','../jove/Def_md2mc.py',595),
  ('one_label -> ID_or_EPS_or_B SEMICOLON ID_or_EPS_or_B COMMA ID_or_EPS_or_B','one_label',5,'p_one_label3','../jove/Def_md2mc.py',617),
]
