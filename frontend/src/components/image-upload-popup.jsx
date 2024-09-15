"use client";

import { useState } from "react";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Button } from "@/components/ui/button";
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogDescription, DialogTrigger } from "@/components/ui/dialog";
import { Upload, Camera, ImagePlus } from "lucide-react";

export function ImageUploadPopup({ reloadPills }) {
  const [uploadedImage, setUploadedImage] = useState(null);
  const [capturedImage, setCapturedImage] = useState(null);
  const [isOpen, setIsOpen] = useState(false);
  const [uploadedImages, setUploadedImages] = useState([]);

  // States for each column in the SQL table
  const [prescriptionName, setPrescriptionName] = useState("");
  const [rawInstruction, setRawInstruction] = useState("");
  const [expirationDate, setExpirationDate] = useState("");
  const [expectedTime1, setExpectedTime1] = useState("");
  const [expectedTime2, setExpectedTime2] = useState("");
  const [expectedTime3, setExpectedTime3] = useState("");

  // Handle image upload
  const handleFileUpload = (event) => {
    const files = event.target.files;
    if (files.length > 0) {
      const imageFiles = Array.from(files);
      const newImages = imageFiles.map((file) => {
        const reader = new FileReader();
        return new Promise((resolve) => {
          reader.onload = (e) => resolve(e.target?.result);
          reader.readAsDataURL(file);
        });
      });
      Promise.all(newImages).then((imageData) =>
        setUploadedImages((prev) => [...prev, ...imageData])
      );
    }
  };

  // Handle image capture
  const handleCapture = (event) => {
    const file = event.target.files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => setCapturedImage(e.target?.result);
      reader.readAsDataURL(file);
    }
  };

  // Submitting form data to the backend
  const handleSubmit = async () => {
    // Create the form data object with SQL column names
    const formData = {
      prescription_name: prescriptionName,
      raw_instruction: rawInstruction,
      expiration_date: expirationDate,
      expected_time1: expectedTime1,
      expected_time2: expectedTime2,
      expected_time3: expectedTime3,
    };

    // Send data to the backend using POST request
    try {
      const response = await fetch('http://localhost:5000/input_data', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error(`Error: ${response.status} ${response.statusText}`);
      }

      const result = await response.json();
      console.log(result);  // Log the backend response

      alert("Data submitted successfully!");

      // Call the reloadPills function to fetch the updated data
      reloadPills();

    } catch (error) {
      console.error("Error submitting data:", error);
    }

    // Close the dialog after submission
    setIsOpen(false);
  };

  return (
    <Dialog open={isOpen} onOpenChange={setIsOpen}>
      <DialogTrigger asChild>
        <Button className="flex items-center space-x-2">
          <ImagePlus className="w-4 h-4" />
          <span>Add Image or Details</span>
        </Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-[425px] md:max-w-[700px]">
        <DialogHeader>
          <DialogTitle>Image Upload or Manual Entry</DialogTitle>
          <DialogDescription>Choose how you want to provide the information</DialogDescription>
        </DialogHeader>
        <Tabs defaultValue="upload" className="w-full">
          <TabsList className="grid w-full grid-cols-3">
            <TabsTrigger value="upload">Upload Image</TabsTrigger>
            <TabsTrigger value="capture">Take Picture</TabsTrigger>
            <TabsTrigger value="manual">Manual Entry</TabsTrigger>
          </TabsList>

          {/* Upload Tab */}
          <TabsContent value="upload">
            <div className="flex flex-col items-center space-y-4 pt-4">
              <Label htmlFor="image-upload" className="w-full">
                <div
                  className="flex flex-col items-center justify-center w-full h-64 border-2 border-dashed rounded-lg cursor-pointer hover:bg-gray-50">
                  <Upload className="w-12 h-12 text-gray-400" />
                  <p className="mt-2 text-sm text-gray-500">Click to upload or drag and drop</p>
                </div>
                <Input
                  id="image-upload"
                  type="file"
                  accept="image/*"
                  className="hidden"
                  onChange={handleFileUpload} />
              </Label>
              {uploadedImages.length > 0 && (
                <div className="mt-4 grid grid-cols-3 gap-2">
                  {uploadedImages.map((image, index) => (
                    <img
                      key={index}
                      src={image}
                      alt={`Uploaded ${index + 1}`}
                      className="max-w-full h-auto rounded-lg"
                      style={{ maxHeight: "200px" }}
                    />
                  ))}
                </div>
              )}
            </div>
          </TabsContent>

          {/* Manual Entry Tab */}
          <TabsContent value="manual">
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
          </TabsContent>
        </Tabs>
        <div className="mt-6">
          <Button className="w-full" onClick={handleSubmit}>Submit</Button>
        </div>
      </DialogContent>
    </Dialog>
  );
}
