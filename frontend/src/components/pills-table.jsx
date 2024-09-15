'use client';
import { useState, useEffect } from 'react';
import { Button } from "@/components/ui/button";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { ImageUploadPopup } from "./image-upload-popup";

export function PillsTableComponent() {
  const [filter, setFilter] = useState("'all'");
  const [pills, setPills] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Function to fetch pills from the backend
  const fetchPills = async () => {
    try {
      const response = await fetch('http://localhost:5000/pills', {
        method: 'POST',  // Using POST to fetch data
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ filter: "all" }) // Example data sent in the POST request (if applicable)
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

  // Fetch pills when the component is mounted
  useEffect(() => {
    fetchPills();
  }, []);

  const filteredPills = filter === 'today'
    ? pills.filter(pill => pill.expiry === "2024-09-14") // Example condition for today's pills
    : pills;

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
            variant={filter === 'today' ? "default" : "outline"}
            onClick={() => setFilter('today')}>
            Today
          </Button>
          <Button
            variant={filter === "'all'" ? "default" : "outline"}
            onClick={() => setFilter("'all'")}>
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
            <TableHead className="font-bold">Name</TableHead>
            <TableHead className="font-bold">Instruction</TableHead>
            <TableHead className="font-bold">Expiry</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {filteredPills.map((pill, index) => (
            <TableRow key={index} className="bg-red-700 text-white">
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
