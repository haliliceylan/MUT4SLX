from matlab.engine import matlabengine



def parse_str(number):
    try:
        return int(number)
    except ValueError:
        return float(number)
    
###################################################################
#
#
#
###################################################################
class MutationIterator:
    def load(self, block: str, eng: matlabengine.MatlabEngine):
        """Load Original Block"""
        pass

    def __iter__(self):
        return self
    
    def __next__(self):
        return self.next_mutant()
    
    def next_mutant(self):
        pass
    
    def get_original(self):
        return ()
        


class SingleParameterMutationIterator(MutationIterator):
    mutant_types = []
    param_name = ""
    unique_original_function = False
    block_type = ""
    current_index = -99
    start_index = -99
    original_function = None
    initialized = False
    
    
    def __iter__(self):
        self.current_index = 0 if self.unique_original_function else 1 # just skip start_index if this is not a unique_orginal_function like if 
        return self
    
    def load(self, block: str, eng: matlabengine.MatlabEngine):
        self.initialized = True
        self.original_function = eng.get_param(block, self.param_name)
        try:
            self.start_index = self.mutant_types.index(self.original_function)
        except ValueError:
            # some blocks has unique original values just store it.
            if self.unique_original_function:
                self.start_index = -1
                return True
            return False
        return True
        
    def next_mutant(self):
        if self.current_index < len(self.mutant_types):
            index = (self.start_index + self.current_index) % len(self.mutant_types)
            self.current_index += 1
            return (self.param_name, self.mutant_types[index])
        else:
            raise StopIteration
            
    def get_original(self):
        return (self.param_name, self.original_function)
    
    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        if not self.initialized:
            return f"{self.__class__.__name__}({self.param_name}, {len(self.mutant_types)})"
        current_mutation_index = (self.start_index + self.current_index - 1) % len(self.mutant_types)
        current_mutation = self.mutant_types[current_mutation_index]
        return f"{self.__class__.__name__}(parameter_name='{self.param_name}', original_value='{self.original_function}', mutation='{current_mutation}', n='{self.current_index-1}/{len(self.mutant_types)-1}')"

    

class MinMaxMutationIterator(SingleParameterMutationIterator):
    mutant_types = ["max", "min"]
    param_name = "function"
    block_type = "MinMax"
            
            
class DoubleInputRelationalOperatorMutationIterator(SingleParameterMutationIterator):
    mutant_types = ["==", "~=", "<", "<=", ">=", ">"]
    param_name = "Operator"
    block_type = "RelationalOperator"
    
    
            
            
#class SingleInputRelationalOperatorMutationIterator(SingleParameterMutationIterator):
#    mutant_types = ["isInf", "isNaN", "isFinite"]
#    param_name = "function"


            
# TODO: there can be more than two sign or less            
class SumMutationIterator(SingleParameterMutationIterator):
    mutant_types = ["++", "+-", "-+", "--"]
    param_name = "Inputs"
    block_type = "Sum"
    
    
class OneSpaceSumMutationIterator(SingleParameterMutationIterator):
    mutant_types = ["|++", "|+-", "|-+", "|--"]
    param_name = "Inputs"
    block_type = "Sum"


        
# TODO: "NOT" function is not supporting because have only 1 input    
class LogicalOperatorMutationIterator(SingleParameterMutationIterator):
    mutant_types = ['AND', 'OR', 'NAND', 'NOR', 'XOR', 'NXOR']
    param_name = "Operator"
    block_type = "Logic"
    
    
class IfMutationIterator(SingleParameterMutationIterator):
    mutant_types = ["1 == 1", "1 == 0"] #instad of true or false
    param_name = "IfExpression"
    unique_original_function = True
    block_type = "If"
    

class TrigonometryMutationIterator(SingleParameterMutationIterator):
    mutant_types = ['sin', 'cos', 'tan','asin','acos','atan','sinh', 'cosh','tanh','asinh','acosh','atanh','cos + jsin'] 
    param_name = "Operator"
    block_type = "Trigonometry"
    


class SingleInputMathMutationIterator(SingleParameterMutationIterator):
    mutant_types = ['exp', 'log','10^u','log10','magnitude^2','square','conj','reciprocal','transpose' ,'hermitian'] 
    param_name = "Operator"
    block_type = "Math"

class DoubleInputMathMutationIterator(SingleParameterMutationIterator):
    mutant_types = ['pow','hypot','rem','mod'] 
    param_name = "Operator"
    block_type = "Math"

    
class ProductMutationIterator(SingleParameterMutationIterator):
    mutant_types = ['Element-wise(.*)', 'Matrix(*)'] 
    param_name = "Multiplication"
    block_type = "Product"

class ProductInputsIterator(SingleParameterMutationIterator):
    mutant_types = ['2', '*/', '/*', '//'] 
    param_name = "Inputs"
    block_type = "Product" 
    
class ForIteratorMutationIterator(SingleParameterMutationIterator):
    mutant_types = ['Zero-based', 'One-based'] 
    param_name = "IndexMode"
    block_type = "ForIterator"


class UnitDelayMutationIterator(SingleParameterMutationIterator):
    mutant_types = ['Columns as channels (frame based)', 'Elements as channels (sample based)'] 
    param_name = "InputProcessing"
    block_type = "UnitDelay"


class SwitchMutationIterator(SingleParameterMutationIterator):
    mutant_types = ['u2 >= Threshold', 'u2 ~= 0'] # discarded.  u2 > Threshold
    param_name = "Criteria"
    block_type = "Switch" 

###################################################################
#
#
#
###################################################################


class SingleParameterLambdaMutationIterator(MutationIterator):
    mutant_types = []
    param_name = ""
    block_type = ""
    current_index = -99
    original_function = None
    initialized = False
    
    
    def __iter__(self):
        self.current_index = 0
        return self
    
    def load(self, block: str, eng: matlabengine.MatlabEngine):
        self.initialized = True
        self.original_function = eng.get_param(block, self.param_name)
        return self.check(eng)
    
    def check(self, eng):
        return True
        
    def next_mutant(self):
        if self.current_index < len(self.mutant_types):
            index = self.current_index
            self.current_index += 1
            val = self.get_val(index)
            return (self.param_name, val)
        else:
            raise StopIteration
            
    def get_val(self,index):
        return str(self.mutant_types[index](parse_str(self.original_function)))
            
    def get_original(self):
        return (self.param_name, self.original_function)
    
    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        if not self.initialized:
            return f"{self.__class__.__name__}({self.param_name}, {len(self.mutant_types)})"
        current_mutation_index = self.current_index-1
        current_mutation = self.get_val(current_mutation_index)
        return f"{self.__class__.__name__}(parameter_name='{self.param_name}', original_value='{self.original_function}', mutation='{current_mutation}', n='{self.current_index}/{len(self.mutant_types)}')"

    

    
    
class ForIteratorLamdaMutationIterator(SingleParameterLambdaMutationIterator):
    mutant_types = [lambda x: x*2] 
    param_name = "IterationLimit"
    block_type = "ForIterator"


class UnitDelayLamdaMutationIterator(SingleParameterLambdaMutationIterator):
    mutant_types = [lambda x: x+10] 
    param_name = "InitialCondition"
    block_type = "UnitDelay"


class SwitchLamdaMutationIterator(SingleParameterLambdaMutationIterator):
    mutant_types = [lambda x: x+10]
    param_name = "Threshold"
    block_type = "Switch"
    
    def check(self, eng):
        # check block is not u2 ~= 0
        return self.original_function != "u2 ~= 0"

    
class ConstantLamdaMutationIterator(SingleParameterLambdaMutationIterator):
    mutant_types = [
        lambda x: x+1, lambda x: x+10, lambda x: x+100,
        lambda x: x-1, lambda x: x-10, lambda x: x-100,
    ]
    param_name = "Value"
    block_type = "Constant" 
    
    def check(self, eng):
        # check value is int or float
        try:
            parse_str(self.original_function)
            return True
        except ValueError:
            return False


###################################################################
#
#
#
###################################################################



class MutationApplier:
    def apply(self, block: str, eng: matlabengine.MatlabEngine, args):
        eng.set_param(block, *args, nargout=0)
        
        
        

###################################################################
#
#
#
###################################################################

