import json

# Import mutation operator classes here
from MutationClasses import (
    MinMaxMutationIterator, 
    DoubleInputRelationalOperatorMutationIterator, 
    SumMutationIterator, 
    LogicalOperatorMutationIterator,
    IfMutationIterator,
    TrigonometryMutationIterator,
    SingleInputMathMutationIterator,
    DoubleInputMathMutationIterator,
    ProductMutationIterator,
    OneSpaceSumMutationIterator,
    ForIteratorMutationIterator,
    UnitDelayMutationIterator,
    SwitchMutationIterator,
    ForIteratorLamdaMutationIterator,
    UnitDelayLamdaMutationIterator,
    SwitchLamdaMutationIterator,
    ConstantLamdaMutationIterator,
    ProductInputsIterator
)


def get_available_mutant_operators(config):
    """Load list of available mutation operators from a configuration file.
    
    Args:
        config (dict): configuration object containing a list of short names for mutation operators.
    
    Returns:
        List[Type]: List of mutation operator classes corresponding to the short names in the configuration file.
    """
    # Define mapping of short names to mutation operators
    mutation_operator_map = {
        "ROR": DoubleInputRelationalOperatorMutationIterator,
        "LOR": LogicalOperatorMutationIterator,
        "ASR": (SumMutationIterator, OneSpaceSumMutationIterator),
        "MMR": MinMaxMutationIterator,
        "ICR": IfMutationIterator,
        "TOR": TrigonometryMutationIterator,
        "MOR": (SingleInputMathMutationIterator, DoubleInputMathMutationIterator),
        "PMR": ProductMutationIterator,
        "POR": ProductInputsIterator,
        "FIR": ForIteratorMutationIterator,
        "FLR": ForIteratorLamdaMutationIterator,
        "UDO": (UnitDelayMutationIterator, UnitDelayLamdaMutationIterator),
        "SCR": SwitchMutationIterator,
        "STR": SwitchLamdaMutationIterator,
        "CR": ConstantLamdaMutationIterator
    }

    short_names = config["mutant_operators"]
    available_mutant_operators = []
    short_list = []
    for short_name in short_names:
        if short_name in mutation_operator_map:
            short_list.append(short_name)
            mutation_operator = mutation_operator_map[short_name]
            if isinstance(mutation_operator, tuple):
                available_mutant_operators.extend(mutation_operator)
            else:
                available_mutant_operators.append(mutation_operator)

    return available_mutant_operators,short_list