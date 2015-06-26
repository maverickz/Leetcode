package main;
/**
 * @author Karthik Raj
 *
 */
public class PrintFactors {

	/**
	 * Prints all possible factors which when multiplied produces the number 'num', without repetition of factors
	 * i.e for instance if num is 12, the output cannot contain both 4 * 3 and 3 * 4 as they are duplicates formed 
	 * by the same factors in different order.
	 * Note: The input number is assumed to be a positive integer
	 * 
	 * @param num         the integer number to be factorized
	 * @param lastFactor  last factor present in the prefix, if the prefix is empty last factor is same as num
	 * @param prefix	  string containing one or more partial factors of the original number, the factors are in ascending order
	 */
	public void factors(int num, int lastFactor, String prefix) {
		if (num < 0) {
			System.out.println("Expected positive integer, given "+num);
			return;
		}
		for (int i = num; i > 1; i--) {
			int remainder = num % i;
			if (remainder == 0) {
				int quotient = num / i;
				if (quotient == 1) {
					continue;
				}
				/*
				 * If 'i' is a factor of 'num' recursively find all possible multipliers of the resultant quotient under the 
				 * following constraints
				 * - quotient should be smaller than 'i' so that the factors are in ascending order in the resultant prefix
				 *   to avoid duplicates, by forcing a 'multiplier' which can further be decomposed into sub-multipliers,
				 *   only once
				 * - quotient is smaller than 'num', this eliminates duplicate processing a factor larger than 'num' in the current 
				 *   recursive call, would have already been processed in an earlier recursive call, since the factors are processed
				 *   in order
				 * - lastfactor is an indicator to maintain the order of factors in the prefix, i.e any resultant decomposition which 
				 *   has at least one factor which is larger than the lastfactor from the previous decomposition can safely be skipped
				 *   as already being processed 
				 */
				if (quotient <= i && quotient <= num) {
					if (i <= lastFactor && quotient <= lastFactor) {
						if (prefix.length() > 0) {
							System.out.println(prefix+""+i+" * "+quotient);
						} else {
							System.out.println(i+" * "+quotient);
						}
					}
				}
				if (i <= lastFactor) {
					factors(quotient, i, prefix+i+" * ");
				}
			}
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int num;
		PrintFactors printObj = new PrintFactors();
		if (args.length > 0) {
		    try {
		        num = Integer.parseInt(args[0]);
		        System.out.println(num+" * 1");
		        printObj.factors(num, num, "");
		    } catch (NumberFormatException e) {
		        System.err.println("Argument" + args[0] + " must be an integer");
		        System.exit(1);
		    }
		}
	}
}
 