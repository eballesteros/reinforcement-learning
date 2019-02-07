import unittest
from tic_tac_toe import Enviroment, Agent
from tic_tac_toe_helpers import add_multiple_points, state_to_board

class TestEnviroment(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
    
    def setUp(self):
        self.env_empty = Enviroment()
        
        self.env_won_v = Enviroment()
        add_multiple_points(self.env_won_v,[(0,0),(0,1),(0,2)],[1,1,1])
        
        self.env_won_h = Enviroment()
        add_multiple_points(self.env_won_h,[(0,0),(1,0),(2,0)],[1,1,1])
        
        self.env_won_dpos = Enviroment()           
        add_multiple_points(self.env_won_dpos,[(0,0),(1,1),(2,2)],[1,1,1])
        
        self.env_won_dneg = Enviroment()           
        add_multiple_points(self.env_won_dneg,[(0,2),(1,1),(2,0)],[1,1,1])
        
        self.env_not_won = Enviroment()
        add_multiple_points(self.env_not_won,[(2,2),(1,1),(0,0)],[1,2,1])
    
    def tearDown(self):
        pass
    
    def test_player_won(self):    
        self.assertTrue(self.env_won_v.player_won(1))
        self.assertTrue(self.env_won_h.player_won(1))
        self.assertTrue(self.env_won_dpos.player_won(1))
        self.assertTrue(self.env_won_dneg.player_won(1))
        
        self.assertFalse(self.env_won_v.player_won(2))
        self.assertFalse(self.env_won_h.player_won(2))
        self.assertFalse(self.env_won_dpos.player_won(2))
        self.assertFalse(self.env_won_dneg.player_won(2))
        
        self.assertFalse(self.env_empty.player_won(1))
        self.assertFalse(self.env_not_won.player_won(1))
        
    def test_get_empty_spots(self):
        all_points = {(x,y) for x in range(3) for y in range(3)}
        
        self.assertEqual(self.env_empty.get_empty_spots(), all_points) 
        
        self.assertEqual(self.env_won_v.get_empty_spots(), all_points - {(0,0),(0,1),(0,2)})
        
        self.assertEqual(self.env_won_h.get_empty_spots(), all_points - {(0,0),(1,0),(2,0)})
        
        self.assertEqual(self.env_won_dpos.get_empty_spots(), all_points - {(0,0),(1,1),(2,2)})
        
        self.assertEqual(self.env_won_dneg.get_empty_spots(), all_points - {(0,2),(1,1),(2,0)})
        
        self.assertEqual(self.env_not_won.get_empty_spots(), all_points - {(2,2),(1,1),(0,0)})
        
    def test_get_state(self):
        
        self.assertEqual(self.env_empty.get_state(),0)
        
        self.assertEqual(self.env_won_v.get_state(),3**0+3**3+3**6 )
        
        self.assertEqual(self.env_won_h.get_state(),3**0+3**1+3**2 )
        
        self.assertEqual(self.env_won_dpos.get_state(),3**0+3**4+3**8 )
        
        self.assertEqual(self.env_won_dneg.get_state(),3**2+3**4+3**6 )
        
        self.assertEqual(self.env_not_won.get_state(),3**0+2*3**4+3**8 )
        
class TestHelpers(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
    
    def setUp(self):
        self.env_empty = Enviroment()
        
        self.env_won_v = Enviroment()
        add_multiple_points(self.env_won_v,[(0,0),(0,1),(0,2)],[1,1,1])
        
        self.env_won_h = Enviroment()
        add_multiple_points(self.env_won_h,[(0,0),(1,0),(2,0)],[1,1,1])
        
        self.env_won_dpos = Enviroment()           
        add_multiple_points(self.env_won_dpos,[(0,0),(1,1),(2,2)],[1,1,1])
        
        self.env_won_dneg = Enviroment()           
        add_multiple_points(self.env_won_dneg,[(0,2),(1,1),(2,0)],[1,1,1])
        
        self.env_not_won = Enviroment()
        add_multiple_points(self.env_not_won,[(2,2),(1,1),(0,0)],[1,2,1])
    
    def tearDown(self):
        pass
    
    def test_state_to_board(self):
        
        self.assertTrue((state_to_board(self.env_empty.get_state()) == self.env_empty.board).all())
        
        self.assertTrue((state_to_board(self.env_won_v.get_state()) == self.env_won_v.board).all())
        
        self.assertTrue((state_to_board(self.env_won_h.get_state()) == self.env_won_h.board).all())
        
        self.assertTrue((state_to_board(self.env_won_dpos.get_state()) == self.env_won_dpos.board).all())
        
        self.assertTrue((state_to_board(self.env_won_dneg.get_state()) == self.env_won_dneg.board).all())
        
        self.assertTrue((state_to_board(self.env_not_won.get_state()) == self.env_not_won.board).all())
    
    
        
        
if __name__ == '__main__':
    unittest.main()
        
        

    
    
    