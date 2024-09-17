'use client';
import { useState, useEffect } from 'react';
import { Button } from "@/components/ui/button";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { ImageUploadPopup } from "./image-upload-popup";

/*
this doesnt work correctly. need to fix this
*/

export function PillsTableComponent() {
  const [filter, setFilter] = useState('all');
  const [pills, setPills] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedImages, setSelectedImages] = useState([]); 
  const [checkedPills, setCheckedPills] = useState({ morning: [], afternoon: [], evening: [] }); 

  const fetchPills = async () => {
    try {
      const response = await fetch('http://localhost:5000/pills', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ filter: 'all' }) 
      });
  
      if (!response.ok) {
        throw new Error(`Error: ${response.status} ${response.statusText}`);
      }
  
      const data = await response.json();
      setPills(data.data);
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchPills();
  }, []);
  const extractHour = (timeString) => {
    return timeString ? parseInt(timeString.split(" ")[1].split(":")[0]) : null;
  };


  const filteredPills = pills.filter((pill) => {
    const hour1 = extractHour(pill.expected_time1);
    const hour2 = extractHour(pill.expected_time2);
    const hour3 = extractHour(pill.expected_time3);

    if (filter === 'morning') {
      return (hour1 >= 6 && hour1 <= 11) || (hour2 >= 6 && hour2 <= 11) || (hour3 >= 6 && hour3 <= 11);
    }
    if (filter === 'afternoon') {
      return (hour1 >= 12 && hour1 <= 16) || (hour2 >= 12 && hour2 <= 16) || (hour3 >= 12 && hour3 <= 16);
    }
    if (filter === 'evening') {
      return (hour1 >= 17 && hour1 <= 21) || (hour2 >= 17 && hour2 <= 21) || (hour3 >= 17 && hour3 <= 21);
    }
    return true; // 'all' filter, return all pills
  });

  // Handle checkbox toggle for each pill
  const handleCheck = (prescriptionName) => {
    const currentChecked = [...checkedPills[filter]]; // Copy the current checked pills for the active filter
    const isChecked = currentChecked.includes(prescriptionName);

    if (isChecked) {
      // If it's already checked, remove it
      setCheckedPills({
        ...checkedPills,
        [filter]: currentChecked.filter(pill => pill !== prescriptionName)
      });
    } else {
      // If it's not checked, add it
      setCheckedPills({
        ...checkedPills,
        [filter]: [...currentChecked, prescriptionName]
      });
    }
  };

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div className="container mx-auto p-4">
      <div className="flex justify-between items-center mb-4">
        <div className="space-x-2">
          <Button
            variant={filter === 'morning' ? "default" : "outline"}
            onClick={() => setFilter('morning')}>
            Morning
          </Button>
          <Button
            variant={filter === 'afternoon' ? "default" : "outline"}
            onClick={() => setFilter('afternoon')}>
            Afternoon
          </Button>
          <Button
            variant={filter === 'evening' ? "default" : "outline"}
            onClick={() => setFilter('evening')}>
            Evening
          </Button>
          <Button
            variant={filter === 'all' ? "default" : "outline"}
            onClick={() => setFilter('all')}>
            All
          </Button>
        </div>
        <h1 className="text-2xl font-bold">Pills</h1>

        {/* Pass the reloadPills function to ImageUploadPopup */}
        <ImageUploadPopup reloadPills={fetchPills}/> 
      </div>

      <Table>
        <TableHeader>
          <TableRow className="bg-black text-white">
            {filter !== 'all' && <TableHead className="font-bold">Select</TableHead>}
            <TableHead className="font-bold">Name</TableHead>
            <TableHead className="font-bold">Instruction</TableHead>
            <TableHead className="font-bold">Expiration Date</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {filteredPills.map((pill, index) => (
            <TableRow key={index} className="bg-red-700 text-white">
              {filter !== 'all' && (
                <TableCell>
                  <input
                    type="checkbox"
                    checked={checkedPills[filter]?.includes(pill.prescription_name)}
                    onChange={() => handleCheck(pill.prescription_name)}
                  />
                </TableCell>
              )}
              <TableCell>{pill.prescription_name}</TableCell>
              <TableCell>{pill.raw_instruction}</TableCell>
              <TableCell>{pill.expiration_date}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  );
}
