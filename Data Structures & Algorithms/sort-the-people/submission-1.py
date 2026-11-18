class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Step 1: Link each height to the person's name
        height_map = dict(zip(heights, names))
        
        # Step 2: Sort the heights from tallest to shortest
        heights.sort(reverse=True)
        
        # Step 3: Build the final list of names in that sorted order
        sorted_names = []
        for height in heights:
            sorted_names.append(height_map[height])
            
        return sorted_names