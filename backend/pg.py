"use client";

import { useState } from "react";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Button } from "@/components/ui/button";

export function ImageUploadPopup({ reloadPills }) {
  const [uploadedImage, setUploadedImage] = useState(null);
  const [ocrResult, setOcrResult] = useState({});
  const [isOpen, setIsOpen] = useState(false);

  // States for each column in the SQL table
  const [prescriptionName, setPrescriptionName] = useState("");
  const [rawInstruction, setRawInstruction] = useState("");
  const [expirationDate, setExpirationDate] = useState("");
  const [expectedTime1, setExpectedTime1] = useState("");
  const [expectedTime2, setExpectedTime2] = useState("");
  const [expectedTime3, setExpectedTime3] = useState("");

  // Handle image upload and OCR processing
  const handleFileUpload = async (event) => {
    const files = event.target.files;
    if (files.length > 0) {
      const formData = new FormData();
      formData.append("images", files[0]);

      try {
        // Call the backend OCR API
        const response = await fetch("http://localhost:5000/scan", {
          method: "POST",
          body: formData,
        });

        if (!response.ok) {
          throw new Error(`Error: ${response.status} ${response.statusText}`);
        }

        const result = await response.json();
        console.log(result); // The result will contain the OCR and LLM data

        // Set the OCR result into the appropriate fields
        setOcrResult(result);
        setPrescriptionName(result.prescription_name || "");
        setRawInstruction(result.raw_instruction || "");
        setExpirationDate(result.expiration_date || "");
        setExpectedTime1(result.expected_time1 || "");
        setExpectedTime2(result.expected_time2 || "");
        setExpectedTime3(result.expected_time3 || "");

        alert("OCR processed and data pre-filled!");

      } catch (error) {
        console.error("Error processing OCR:", error);
      }
    }
  };

  // Submitting form data to the backend
  const handleSubmit = async () => {
    const formData = {
      prescription_name: prescriptionName,
      raw_instruction: rawInstruction,
      expiration_date: expirationDate,
      expected_time1: expectedTime1,
      expected_time2: expectedTime2,
      expected_time3: expectedTime3,
    };

    try {
      const response = await fetch("http://localhost:5000/input_data", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error(`Error: ${response.status} ${response.statusText}`);
      }

      const result = await response.json();
      console.log(result);

      alert("Data submitted successfully!");
      reloadPills();
      setIsOpen(false);

    } catch (error) {
      console.error("Error submitting data:", error);
    }
  };

  return (
    <div>
      <Label htmlFor="image-upload">Upload Prescription Image</Label>
      <Input id="image-upload" type="file" accept="image/*" onChange={handleFileUpload} />
      
      <form className="space-y-4 pt-4">
        <div className="space-y-2">
          <Label htmlFor="prescription_name">Prescription Name</Label>
          <Input
            id="prescription_name"
            placeholder="Enter prescription name"
            value={prescriptionName}
            onChange={(e) => setPrescriptionName(e.target.value)}
          />
        </div>
        <div className="space-y-2">
          <Label htmlFor="raw_instruction">Instructions</Label>
          <Input
            id="raw_instruction"
            placeholder="Enter instructions"
            value={rawInstruction}
            onChange={(e) => setRawInstruction(e.target.value)}
          />
        </div>
        <div className="space-y-2">
          <Label htmlFor="expiration_date">Expiration Date</Label>
          <Input
            id="expiration_date"
            type="date"
            value={expirationDate}
            onChange={(e) => setExpirationDate(e.target.value)}
          />
        </div>
        <div className="space-y-2">
          <Label htmlFor="expected_time1">Expected Time 1</Label>
          <Input
            id="expected_time1"
            placeholder="Enter expected time 1"
            value={expectedTime1}
            onChange={(e) => setExpectedTime1(e.target.value)}
          />
        </div>
        <div className="space-y-2">
          <Label htmlFor="expected_time2">Expected Time 2</Label>
          <Input
            id="expected_time2"
            placeholder="Enter expected time 2"
            value={expectedTime2}
            onChange={(e) => setExpectedTime2(e.target.value)}
          />
        </div>
        <div className="space-y-2">
          <Label htmlFor="expected_time3">Expected Time 3</Label>
          <Input
            id="expected_time3"
            placeholder="Enter expected time 3"
            value={expectedTime3}
            onChange={(e) => setExpectedTime3(e.target.value)}
          />
        </div>
      </form>

      <Button onClick={handleSubmit}>Submit</Button>
    </div>
  );
}
