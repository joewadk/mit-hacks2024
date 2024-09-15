'use client';
import { useState } from 'react'
import { Button } from "@/components/ui/button"
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"
import {ImageUploadPopup} from "./image-upload-popup"

export function PillsTableComponent() {
  const [filter, setFilter] = useState("'all'")
  const [pills, setPills] = useState([
    { name: "Prescription A", instruction: "Take twice daily", expiry: "2023-12-31" },
    { name: "Prescription B", instruction: "Take with food", expiry: "2024-09-14" },
  ])

  const filteredPills = filter === 'today'
    ? pills.filter(pill => {
        return pill.expiry == "2024-09-14";
      })
    : pills;

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
        <ImageUploadPopup/>
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
              <TableCell>{pill.name}</TableCell>
              <TableCell>{pill.instruction}</TableCell>
              <TableCell>{pill.expiry}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  );
}